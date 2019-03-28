import sys
import re

def get_data(data):
	newlines = []
	for line in data:
		line = line.strip('}\n').split(',')
		vals = [s.split(':')[1] for s in line]
		newlines.append(vals)
	keys = [s.split(':')[0] for s in line]
	keys[0] = keys[0][1:]
	print(line)
	return newlines,keys

def output_data(lines,go,cost,dirichlet,pp,filename,keys):
	outputfile = filename.replace('txt','csv')
	lineEnd = [go,cost,dirichlet,pp+'\n']
	
	with open(outputfile,'w') as of:
		for l in lines:
			lineList = l+lineEnd
			line = ','.join(lineList)
			of.write(line)
	keys+=["go.is.p","pCost","dirWeight","pPrior"]
	with open("key.csv","w") as kf:
		kf.write(','.join(keys)+'\n')
			
def main():
	if len(sys.argv) < 6:
  		print("Usage: python format.py filename go_is_perspective cost dirichlet pprior")
	else:
		go = sys.argv[2]
		cost = sys.argv[3]
		dirichlet = sys.argv[4]
		pp = sys.argv[5]
		data = open(sys.argv[1],'r').readlines()
		data = data[0:len(data)-1]
		lines,keys = get_data(data)
		output_data(lines,go,cost,dirichlet,pp,sys.argv[1],keys)

main()