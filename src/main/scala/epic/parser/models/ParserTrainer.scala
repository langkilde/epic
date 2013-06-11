package epic.parser.models

/*
 Copyright 2012 David Hall

 Licensed under the Apache License, Version 2.0 (the "License")
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

 http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
*/
import epic.framework._
import epic.parser.{SimpleChartParser, GenerativeParser, Parser}
import breeze.linalg._
import breeze.optimize._
import epic.trees.AnnotatedLabel
import breeze.config.Help
import com.typesafe.scalalogging.log4j.Logging
import epic.parser.projections.{ReachabilityProjection, ParserChartConstraintsFactory}
import epic.util.CacheBroker
import epic.parser.ParserParams.XbarGrammar
import breeze.util._
import epic.trees.annotations.StripAnnotations
import epic.trees.TreeInstance
import breeze.optimize.FirstOrderMinimizer.OptParams
import epic.parser.ParseEval.Statistics
import java.io.File
import epic.constraints.CachedChartConstraintsFactory
import breeze.util.Implicits._


/**
 * The main entry point for training discriminative parsers.
 * Has a main method inherited from ParserPipeline.
 * Use --help to see options, or just look at the Params class.
 *
 *
 */
object ParserTrainer extends epic.parser.ParserPipeline with Logging {

  case class Params(@Help(text="What parser to build. LatentModelFactory,StructModelFactory,LexModelFactory,SpanModelFactory")
                    modelFactory: ParserExtractableModelFactory[AnnotatedLabel, String],
                    @Help(text="Name for the parser for saving and logging. will be inferrred if not provided.")
                    name: String = null,
                    implicit val cache: CacheBroker,
                    @Help(text="path for a baseline parser for computing constraints. will be built automatically if not provided.")
                    parser: File = null,
                    opt: OptParams,
                    @Help(text="How often to run on the dev set.")
                    iterationsPerEval: Int = 100,
                    @Help(text="How many iterations to run.")
                    maxIterations: Int = 1002,
                    @Help(text="How often to look at a small set of the dev set.")
                    iterPerValidate: Int = 30,
                    @Help(text="How many threads to use, default is to use whatever Scala thinks is best.")
                    threads: Int = -1,
                    @Help(text="Should we randomize weights? Some models will force randomization.")
                    randomize: Boolean = false,
                    @Help(text="Should we enforce reachability? Can be useful if we're pruning the gold tree.")
                    enforceReachability: Boolean = true,
                    @Help(text="Should we check the gradient to make sure it's coded correctly?")
                    checkGradient: Boolean = false)
  protected val paramManifest = manifest[Params]

  def trainParser(trainTrees: IndexedSeq[TreeInstance[AnnotatedLabel, String]],
                  validate: (Parser[AnnotatedLabel, String]) => Statistics, params: Params) = {
    import params._

//    if(threads >= 1)
//      collection.parallel.ForkJoinTasks.defaultForkJoinPool.setParallelism(params.threads)

    val initialParser = params.parser match {
      case null =>
        GenerativeParser.annotated(XbarGrammar(), new StripAnnotations[String](), trainTrees)
      case f =>
        readObject[SimpleChartParser[AnnotatedLabel, String]](f)
    }

    val uncached = new ParserChartConstraintsFactory[AnnotatedLabel, String](initialParser.augmentedGrammar, {(_:AnnotatedLabel).isIntermediate})
    val constraints = new CachedChartConstraintsFactory[AnnotatedLabel, String](uncached)

    val proj = new ReachabilityProjection(initialParser.grammar, initialParser.lexicon)
    val theTrees: IndexedSeq[TreeInstance[AnnotatedLabel, String]] = if(!enforceReachability)  {
      trainTrees
    } else {
      trainTrees.par.map(new StripAnnotations).map(ti => ti.copy(tree=proj.forTree(ti.tree, ti.words, constraints.constraints(ti.words)))).seq.toIndexedSeq
    }

    val model = modelFactory.make(theTrees, constraints)

    val obj = new ModelObjective(model, theTrees, params.threads)
    val cachedObj = new CachedBatchDiffFunction(obj)
    val init = obj.initialWeightVector(randomize)
    if(checkGradient)
      GradientTester.test(cachedObj, obj.initialWeightVector(randomize = true), toString={(i: Int) => model.featureIndex.get(i).toString})

    type OptState = FirstOrderMinimizer[DenseVector[Double], BatchDiffFunction[DenseVector[Double]]]#State
    def evalAndCache(pair: (OptState, Int)) {
      val (state, iter) = pair
      val weights = state.x
      if (iter % iterPerValidate == 0) {
        logger.info("Validating...")
        val parser = model.extractParser(weights)
        val stats = validate(parser)
        logger.info("Overall statistics for validation: " + stats)
      }
    }

    val name = Option(params.name).orElse(Option(model.getClass.getSimpleName).filter(_.nonEmpty)).getOrElse("DiscrimParser")

    for ((state, iter) <- params.opt.iterations(cachedObj, init).take(maxIterations).zipWithIndex.tee(evalAndCache _)
         if iter != 0 && iter % iterationsPerEval == 0) yield try {
      val parser = model.extractParser(state.x)
      (s"$name-$iter", parser)
    } catch {
      case e: Exception => e.printStackTrace(); throw e
    }
  }
}