import sys
import re
import json
import math

def get_data(data):
	probDict = {}
	currSent = ''
	for line in data:
		line = line.strip()
		if line[0] != '{':
			currSent = line
			probDict[currSent] = []
		else:
			fields = jsonToPython = json.loads(line)
			worlds = fields['support'][0]['support']
			probs = fields['support'][0]['probs']
			wp_pairs = (worlds,probs)
			assert len(worlds) == len(probs)
			currProbs = probDict[currSent]
			probDict[currSent] = wp_pairs
	return probDict

def sep_data(ddict,fields):
	sents = ddict.keys()
	worldNames = {}
	probDict = {}
	for s in sents:
		probDict[s] = {}
		worlds = ddict[s][0]
		probs = ddict[s][1]
		assert abs(1.0-sum(probs)) <= max(1e-09 * max(abs(1.0), abs(sum(probs))), 0.0)
		for i in range(0,len(worlds)):
			w = worlds[i][0]
			ph = worlds[i][1]['holder']
			p = probs[i]
			wstring = ''
			for f in fields:
				wstring += str(w[f])+','
			wstring += ph

			if wstring not in worldNames:
				worldNames[wstring] = len(worldNames.keys())
			pdict = probDict[s]
			pdict[wstring] = p
        	probDict[s] = pdict
	for s in sents:
		for wstring in worldNames.keys():
			if wstring not in probDict[s]:
				pdict = probDict[s]
				pdict[wstring] = 0.0
				probDict[s] = pdict
	return probDict

def output_data(pDict,go,cost,filename):
	outputfile = filename.replace('txt','csv')
	lineEnd = [go,cost]
	lines = []
	key = ["sentence"]
	sentences = pDict.keys()
	for s in sentences:
		lineStart = s+','
		for w in pDict[s]:
			prob = pDict[s][w]
			lineList = lineStart
			lineList += w+','
			lineList += str(prob)+','
			lineList+= ','.join(lineEnd)
			lines.append(lineList+'\n')
	with open(outputfile,'w') as of:
		for line in lines:
			of.write(line)
	key+=["go.is.p","pCost"]
	with open("key.csv","w") as kf:
		kf.write(','.join(key)+'\n')
			
def main():
	if len(sys.argv) < 4:
  		print "Usage: python format.py filename go_is_perspective cost dirichlet pprior"
	else:
		go = sys.argv[2]
		cost = sys.argv[3]
  		data = open(sys.argv[1],'r').readlines()
		dDict = get_data(data)
		probDict = sep_data(dDict,["locJane","moveSarahNoho","locSarah","moveElizaNoho","moveJaneNoho"])
  		output_data(probDict,go,cost,sys.argv[1])
  		#"locJane","moveS","locSarah", "moveE","moveJ"

main()