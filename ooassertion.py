from __future__ import division
import sys
import re
import itertools
import random
from messageClass import Message
import copy

def expandMessages(u,aList,pList,eDict,gaps):
	messageList = [[u,aList,pList]]
	for gap in gaps:
		subList = eDict[gap]
		newMessageList = []			
		for m in messageList:
			currU = m[0]
			currA = m[1]
			currP = m[2]
			if gap not in currU:
				newMessageList.append(m)
			else:
				for sub in subList:
					newU = re.sub(gap,sub,currU)
					newAList = []
					newPList = []
					for a in range(0,len(currA)):
						newAList.append(re.sub(gap,sub,currA[a]))
					for p in range(0,len(currP)):
						newPList.append(re.sub(gap,sub,currP[p]))
					newMessageList.append([newU,newAList,newPList])
		messageList = newMessageList
	return messageList

def parseMessages(mfile,eDict):
	mDict = {}
	mList = []
	mf = open(mfile,"r")
	messages = mf.read().split("\n")
	for m in messages:
		mContents = m.split("&")
		utterance = mContents[0]
		assertions = mContents[1].split("\t")
		presuppositions = mContents[2].split("\t")
		gaps = mContents[3].split(",")
		expandedMList = expandMessages(utterance,assertions,presuppositions,eDict,gaps)
		for exM in expandedMList:
			mDict,mList = insertMessages(exM,mDict,mList)
	return mDict,mList

def insertMessages(m,mDict,mList):
	u = m[0]
	a = m[1]
	p = m[2]
	mObject = Message(u,a,p)
	mDict[len(mList)] = mObject
	mList.append(mObject)
	return mDict,mList

def parseEntities(efile):
	eDict = {}
	ef = open(efile,"r")
	entLines = ef.read().split("\n")
	for e in entLines:
		entry = e.split("\t")
		name = entry[0]
		entries = entry[1].split(",")
		eDict[name] = entries
	return eDict

def main():
	if len(sys.argv) < 3:
		print "Usage: python assertion.py worlds entities messages"
		quit()
	wfile = sys.argv[1]
	efile = sys.argv[2]
	mfile = sys.argv[3]
	eDict = parseEntities(efile)
	mDict,mList= parseMessages(mfile,eDict)
	for m in mList:
		print m
main()