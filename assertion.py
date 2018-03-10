import sys

def parseEntities(efile):
	ef = open(efile, 'r')
	e = ef.read().split("\t")
	print e

def main():
	wfile = sys.argv[1]
	efile = sys.argv[2]
	pfile = sys.argv[3]

main()

