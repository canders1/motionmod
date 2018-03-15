class Message:
	def __init__(self,string,assertions,presuppositions):
		self.utterance = string
		self.assertions = assertions
		self.presuppositions = presuppositions
		self.cost = 0.0

	def getAssertions(self):
		return self.assertions

	def getPresuppositions(self):
		return self.presuppositions

	def getCost(self):
		return self.cost

	def getUtterance(self):
		return self.utterance