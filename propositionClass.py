class Proposition:
	def __init__(self,string,pred,time,args):
		self.name = string
		self.pred = pred
		self.time = time
		self.args = args

	def __str__(self):
		return self.name