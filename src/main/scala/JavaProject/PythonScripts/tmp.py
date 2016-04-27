#import pymongo 
import sys 
import os 
#from pymongo import MongoClient 
from moveBatch import moveBatch
rString = moveBatch([0.30690298998810017,0.49979693944415127,0.9263564270951724,0.10944997424989089,0.4358116556152565,0.16068460341267132,0.1779537888480872,0.6568323644526609,0.6113606757925146,0.09635441807149703,0.40154561503130115,0.2930667719671137,0.8426974055266959,0.5907245357511487,0.7352612208144537,0.16492444909554016,0.5779393133830614,0.30683184976499045,0.6022158529268236,0.904155971030841,0.6092789449955339,0.08672218484691552,0.6394254936623668,0.6968216898737569,0.0642379299581407,0.28925987950389254,0.8604662714761908,0.22281549150507585,0.24508210391208352,0.336075106837067,0.3765029963471024,0.31009237870140816,0.8737990290169059,0.24067282406382862,0.2579426222833816,0.4209656231644018,0.779012458538885,0.7848524267270344,0.7018150909792341,0.4128783660843466,0.799017837432222,0.5753749328181539,0.39060447056627634,0.17626884762591388,0.6545578366742056,0.45581522707874145,0.6198031527549159,0.5687140382865452,0.983539297564632,0.3672317832306764,0.8744015083182366,0.8017613945633993,0.8834460259423744,0.08188173506397445,0.46577771340179974,0.5086839145186668,0.6952133979734281,0.36740408637019084,0.17358710511102893,0.21109678234074325,0.7288605398272848,0.38160763338813875,0.9122887962855414,0.7355107762979027,0.8405861248229157,0.8512231620503096,0.3485747152886458,0.8833655883566482,0.7817459255427177,0.30246200239034493,0.9591553419640301,0.6835865613085157,0.2192628472463528,0.9721891722190086,0.15601301338032214,0.15943673145191017,0.5881849430862685,0.8582319138737817,0.06391569584727774,0.14668948860746034,0.9700398759115448,0.36710858037405136,0.5412503397678626,0.8944489203467828,0.07390746878822307,0.05021599160415302,0.2872233412802644,0.7487544427909256,0.947859085668096,0.1474082316923221,0.05055930517428775,0.8680092810948458,0.18866845200454874,0.6497560590771542,0.7679092925442264,0.06851285532207863,0.5885601425841733,0.1674612317001909,0.7168211515766437,0.20726584729834352,0.5547789026234423,0.11614323361191836,0.08049877958873497,0.19521994158453915,0.6496347078263083,0.1290287461959564,0.5721928896716525,0.7438813598236051,0.13498751905271733,0.6048181377621498,0.11101013036801799,0.25032234029724687,0.49826769717072295,0.1529240945595548,0.7669776427359929,0.6662486390010578,0.07847467560272803,0.9445858398911964,0.48142790337704267,0.10520565466909759,0.48568225617853666,0.4915257955950837,0.07067863344554226,0.2508788300748217,0.780626743501066,0.9495101662520035,0.5149378779884897,0.7757818415635346,0.3358453916240711,0.055725541042561666,0.758514566358318,0.4014704960439669,0.4965017799284579,0.126510874282301,0.07441029681899047,0.7919678852301397,0.8029508694246211,0.36074770736346806,0.886217970942835,0.8187442725085468,0.5618488821475155,0.7356084938461053,0.8201938863402256,0.6787359112001765,0.6055302640831299,0.4116096843728466,0.3151970350775324,0.5331895003857915,0.9003165008245014,0.3019919665266767,0.7969838943802647,0.18826047383355327,0.6118266987169881,0.7151654081155114,0.9353647617348337,0.9945377052150172,0.22171093961152244,0.46313748842364644,0.9483412722495707,0.06110840618022251,0.24188566638034192,0.8324520489039064,0.7599614214205009,0.7256139449396488,0.6045414238334935,0.7170147343233851,0.7418894888662033,0.8382727537769965,0.2872907226295146,0.3808215091315259,0.34224099951194553,0.7761892960468983,0.7049014191662782,0.924205476128597,0.6707114802720355,0.4478642953337174,0.4558493190451266,0.9691298069542403,0.5862572848813832,0.08409747548094881,0.8693282098719591,0.45792504550593327,0.801580501253228,0.32350822067433205,0.2544526438115966,0.6359565438300123,0.29815169028577193,0.5360185023869334,0.15393035018237122,0.6198837159324107,0.6274705062773779,0.3841428591462739,0.4855437734140159,0.962315630273767,0.79258872442152,0.18677812853977926,0.14378224503428128,0.9852836262415564,0.9322138283903735,0.6595201547324728,0.36640013982757313,0.47673075619438454,0.22104237380199976,0.9723657492106131,0.20638512519824959,0.7056361500367031,0.9643628664832037,0.8695437080566715,0.7066550542574781,0.2962414248087891,0.9374673712865258,0.26323934628684265,0.14602955104583615,0.31804953263535307,0.48988309908084815,0.13139007537441005,0.9639434645357052,0.45559974855264496,0.9996921255614015,0.41511599163213797,0.5957349045804943,0.5021330201404934,0.9897738534977106,0.2445925677788977,0.416545014106793,0.6426931487992482,0.8231274455700728,0.7929214558092932,0.28589620767963186,0.7207307806423132,0.05413063352843228,0.15981188043679462,0.22725880888399175,0.40549983739572504,0.8343181276300244,0.84758352898586,0.19703199155257267,0.705934731564553,0.09902022533527788,0.2795286798379554,0.45091948815856064,0.08888030219787202,0.9394635157737761,0.06950469682889948,0.9763278740199993,0.4404465552065804,0.4427629984086704,0.05686860281009343,0.3714993569231214,0.7949239537146121,0.5845481697772698,0.548885558967749,0.22331979441427785,0.6655881952855084,0.810899260030451,0.3688624360703736,0.3811449453253599,0.10016624428793197,0.7333294773507479,0.4190197103766672,0.18222201532186277,0.4291404883738382,0.9266187462091393,0.8115576526730093,0.2524154992281423,0.4386966357418175,0.4996500448272213,0.588316886631904,0.609809331370355,0.7921254557893884,0.12764461032889673,0.14655125875364605,0.957414219983877,0.15455710804395273,0.10835674717987631,0.7805611945471261,0.30875995330026385,0.16975794387732834,0.6600967751153358,0.728775599518004,0.796521205005136,0.8318390949804007,0.775691541866187,0.3693117875189448,0.41058908089485535,0.9264886214427459,0.2908722725010373,0.7555898168803481,0.9172130438930726,0.9408570300081693,0.43813662345592475,0.729449474835422,0.7900596936912505,0.49394906848839737,0.7388793534982849,0.43356733228967814,0.09888924868579418,0.4926093941607729,0.7860681853158086,0.6099793774464719,0.29425358295598913,0.6849115904935204,0.727734067704175,0.2519115612928856,0.7287546750949999,0.06658679193764538,0.051247005062466267,0.28615995987050846,0.061324592537620015,0.9674420262473135,0.8246765768245323,0.9996571398992232,0.852067259409109,0.8030704569319389,0.46955623983436523,0.24563753367442753,0.39310563864190173,0.2059931632121884,0.2593679493718124,0.983626232748382,0.6703848311276693,0.4418081180256739,0.3112670789264017,0.2525486360161109,0.09306247960185354,0.055789373959346356,0.2593831015061102,0.7941056542178835,0.9920691832136973,0.4070785261362394,0.6808302809623626,0.22839360391062402,0.13205587853317613,0.18674022443526095,0.47616783608909674,0.6586396844274053,0.43871508819878857,0.16451695425285884,0.7208568859963618,0.05395917106394654,0.99507199312403,0.10360210180899998,0.9809192015905756,0.058759422729908306,0.6488562473251915,0.861802594714666,0.6011076342701143,0.978112304030944,0.262799242649816,0.4542804317566983,0.6065821023187472,0.5899445907181778,0.7149942775060165,0.33611103634912376,0.9336836606970246,0.8772687412914755,0.5770150478027717,0.05927277995856994,0.3005724278948615,0.25629235297195785,0.5997403125480159,0.07521712924531798,0.7183821082872722,0.5076968585360003,0.14091044400395347,0.7243727385720069,0.6994908453092417,0.9559064564528323,0.09234155982195924,0.2342642367183937,0.7431125334121388,0.7480668709443303,0.303142015814469,0.910021238254413,0.7982973144165242,0.27094615087336704,0.2431401962982237,0.2554241300902347,0.3872095534510741,0.3024346087915204,0.6909785731011765,0.2957552851992764,0.6246780406111079,0.8445065269913266,0.11141498539245764,0.325767803763895,0.13485147892558724,0.7361130763907695,0.11433549156807343,0.826856823233772,0.22455724365074448,0.11454406836903885,0.6259819748931909,0.8661425436984158,0.06900621098059445,0.11419976880102412,0.8753835891636947,0.14754477999272253,0.125857211754681,0.2811789489752272,0.6353406233659782,0.757415319301276,0.0601037596743087,0.1784197225249572,0.5461430473258188,0.21199536001647534,0.4485419021456142,0.9596536060936389,0.40851866982901663,0.5582600027936598,0.6499758918452994,0.14412567522596909,0.21782428460614178,0.9765530535366694,0.10166001713875128,0.365364454336889,0.6147066286051068,0.8540596749478636,0.4355966634998434,0.676211866746572,0.7478799334664644,0.5584408579368935,0.9907498297648487,0.28673404755091947,0.5434148146717765,0.3373740698592348,0.06264857398121992,0.25394926020180697,0.4964194336413138,0.4982535705142065,0.6610414339882186,0.7196444433777934,0.8302605380399178,0.9441767069159578,0.8698162891963983,0.4809738154576171,0.5570465903130741,0.12837285973234414,0.783589236774856,0.10593857522282168,0.3255519169893393,0.5935838994048357,0.37869413035823607,0.20897964593320406,0.27895086074860553,0.6859052234071917,0.9734268134545576,0.9653086904808982,0.8902740650390508,0.8457821639673381,0.7359978275339342,0.13158232391079105,0.9930109605551234,0.9086180838888628,0.24401846737492694,0.7075230229408094,0.11396519579673059,0.7852817487693611,0.8857245544700649,0.7177914524848746,0.989542938480533,0.06749292047270583,0.1375100271386821,0.2464857484905555,0.39497824412239635,0.15183456808672602,0.19490912736929789,0.21447946029306386,0.32864283398422534,0.12440265080188129,0.7182476035200782,0.7174368082232878,0.3351615178456654,0.688761661244273,0.5493739335456361,0.1924190217273728,0.4726495323418003,0.2722512296010612,0.5137701685334772,0.19743763122720437,0.5289387230947507,0.8179025253596105,0.3611605420250318,0.21554265391142846,0.8018502951344499,0.3022195814182427,0.7304551679307834,0.15506677014067904,0.8745665816963795,0.8666128662672283,0.7550072334644595,0.6903804914760642,0.4780074756563476,0.27966484890344223,0.9326161173226494,0.729996517628418,0.6037981512437133,0.6993716043573502,0.49927590010116696,0.27390711167224946,0.505011763112984,0.7979405997886724,0.40978046694790116,0.44794696000264034,0.27325838230743005,0.23513174748566645,0.6357896082000098,0.9029948745380134,0.11577899019315596,0.7427209673326144,0.2259207050950287,0.5655756892721157,0.7604870226466321,0.46378493115241426,0.9492695671854922,0.05059166090774203,0.8654538655607259,0.5978019149724088,0.48422697712588425,0.7312430778031425,0.2039512387991197,0.47384382055504193,0.7804817734796199,0.7428765230488192,0.9777341449635265,0.6293723418514835,0.21836786488722693,0.6088801796356017,0.5991057631110378,0.5690403907283811,0.44567018334487685,0.3423816265885379,0.9248691643359792,0.14593280594874158,0.5038375665663253,0.22332703634306295,0.2419489093289695,0.16293604533989126,0.20467607401260968,0.16216033572433775,0.31350405200646436,0.05839892057921203,0.5762562325023816,0.4402039243927023,0.34541099601339553,0.8905904021958022,0.24375746606348447,0.6126234802802629,0.8776834021606551,0.8510634738033801,0.8189118767316377,0.9670058435911303,0.5269790729706199,0.9850963464258599,0.2881875387761046,0.31976097200833153,0.154867514376811,0.29251922581869527,0.6793734141907359,0.713472390507612,0.6897227841961494,0.6858049174556098,0.15796728809452887,0.09304272917219192,0.6293539169429643,0.22137043066997097,0.8763407016155524,0.17753335175298968,0.1644281228145552,0.42574176384029594,0.9187148864094975,0.7781051116151886,0.37551484711053384,0.5605928152646739,0.8509989949784653,0.09046235631225041,0.8238087381935919,0.18703587527888166,0.8047317462190386,0.799182124248561,0.24015714769253027,0.06511955076405374,0.977449383336282,0.6753965736029746,0.6820325392195834,0.4579372635170865,0.7896748482429738,0.32341996603312706,0.17098684991903867,0.6459077768187392,0.09961027888470353,0.9865671471898347,0.30953499561563225,0.7453207459712569,0.5266321934439487,0.7655204550593383,0.7647758167766534,0.7126082270202729,0.3469320538292513],0.0)
print str(rString)
