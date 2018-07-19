import sys
import re

def get_data(data):
	probDict = {}
	currSent = ''
	for line in data:
		if line != 'Marginal:\n':
			line = line.strip()
			if line[0] != '{':
				currSent = line
				probDict[currSent] = []
			else:
				currProbs = probDict[currSent]
				if line not in currProbs:
					currProbs.append(line)
					probDict[currSent] = currProbs
	return probDict

def sep_data(ddict):
	sents = ddict.keys()
	worldNames = {}
	probDict = {}
	for s in sents:
		probDict[s] = {}
		assert len(ddict[s]) == 1
		data = ddict[s][0].split(',\"support\":')
		probs = data[0].replace("{\"probs\":","").strip("[]").split(',')
		support = data[1]
		support = support.replace(']]} : 1','').replace('true','True').replace('false','False').strip('[').split('],[')
		for i in range(0,len(support)):
			w = support[i]
			p = probs[i]
			if w not in worldNames:
				worldNames[w] = len(worldNames.keys())
			pdict = probDict[s]
			suptup = eval(w)
			wdict = suptup[0]
			wdict["holder"] = suptup[1]['holder']
			wdict["prob"] = p
			pdict[w] = wdict
        	probDict[s] = pdict
	for s in sents:
		for w in worldNames.keys():
			if w not in probDict[s]:
				pdict = probDict[s]
				suptup = eval(w)
				wdict = suptup[0]
				wdict["holder"] = suptup[1]['holder']
				wdict["prob"] = 0
				pdict[w] = wdict
				probDict[s] = pdict
	return probDict

def output_data(pDict,go,cost,dirichlet,pp,filename):
	outputfile = filename.replace('txt','csv')
	lineEnd = [go,cost,dirichlet,pp]
	lines = []
	key = ["sentence"]
	key += pDict[pDict.keys()[0]][pDict[pDict.keys()[0]].keys()[0]]
	for s in pDict.keys():
		for w in pDict[s].keys():
			lineList = [s]
			for entry in pDict[s][w]:
				lineList.append(str(pDict[s][w][entry]))
			lineList+= lineEnd
			line = ','.join(lineList)
			lines.append(line+'\n')
	with open(outputfile,'w') as of:
		for line in lines:
			of.write(line)
	key+=["go.is.p","pCost","dirWeight","pPrior"]
	with open("key.csv","w") as kf:
		kf.write(','.join(key)+'\n')
			
def main():
	if len(sys.argv) < 6:
  		print "Usage: python format.py filename go_is_perspective cost dirichlet pprior"
	else:
		go = sys.argv[2]
		cost = sys.argv[3]
		dirichlet = sys.argv[4]
		pp = sys.argv[5]
  		data = open(sys.argv[1],'r').readlines()
  		if data[0][0:11] == 'Categorical':
  			priors = data[5]
  			data = data[6:]
  		data = data[0:len(data)-1]
		dDict = get_data(data)
  		probDict = sep_data(dDict)
  		output_data(probDict,go,cost,dirichlet,pp,sys.argv[1])

main()