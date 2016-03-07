import pymongo
import sys
import os
from pymongo import MongoClient
from makeConllFromDBOutput import makeConll
from getJustSentences import getJustSentences

# python will convert \n to os.linesep
def relabelBatch(randomIds,noise):
	returnString = "Tmp file: "
	print "Inside moveBatch"
	# Move Batch between databases
	client = MongoClient('mon-entity-event-r13-2.recfut.com:27016')
	db = client.rf_entity_curation
	labeled = db.malware_labeled
	unlabeled = db.malware_unlabeled
	batch = open(os.path.expanduser("~/epic/epic/data/batch.txt"),'w')
	readlabeled = open(os.path.expanduser("~/epic/epic/data/labeledPool.txt"), 'r')
	lines = readlabeled.readlines()
	readlabeled.close()
	print "Labeled openened for rewriting"
	#print "randomIds "  + str(randomIds)

	################## Batch moved  in database #############
	#for oneId in randomIds:
	#	tmpId = unlabeled.find({"random" : oneId})
	#	labeled.insert(tmpId)
	#	unlabeled.remove({"random" : oneId})
	#	tmpId = labeled.find({"random" : oneId})
	#	batch.write(str(tmpId[0]))
	#	batch.write("\n")

	#print "Starting to remove id from textfile"
	for line in lines:
		idFound = False
		for oneID in randomIds:
			if not (line.find(str(oneID)[0:len(str(oneID))-2])==-1):
				idFound = True
			#print str(idFound)+" " +str(oneID)[0:len(str(oneID))-2] +"\n"+line
		if idFound:
			batch.write(line)
			#print line + " does not include " +oneId
		#print str(idFound)+" " + +"\n"+line
		#returnString += str(idFound) + " " + line + "\n"


	batch.close()


	# Get Conll of the batches and add these to all conll's of labeled pool
	makeConll("~/epic/epic/data/batch.txt", "~/epic/epic/data/batchConll.conll", noise)

	labeledOrig = open(os.path.expanduser("~/epic/epic/data/labeledPool.txt"), 'a')
	labeledOrigConll = open(os.path.expanduser("~/epic/epic/data/labeledPool.conll"),'a')

	batch = open(os.path.expanduser("~/epic/epic/data/batch.txt"),'r')
	batchConll = open(os.path.expanduser("~/epic/epic/data/batchConll.conll"),'r')

	labeledOrig.write(batch.read())
	labeledOrigConll.write(batchConll.read())
	labeledOrig.close()
	labeledOrigConll.close()

	batch.close()
	batchConll.close()

	#os.remove(os.path.expanduser("~/epic/epic/data/batch.txt"))
	#os.remove(os.path.expanduser("~/epic/epic/data/batchConll.conll"))





	return returnString
















