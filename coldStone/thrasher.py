import requests
import json
import threading
import datetime
from hit import hit
from ball import ball

class thrasher(threading.Thread):
	"""A program for creating a certian number of 
	hits, and cause them to thrash the given web site.
	After the hits finish, the program averages the times, and 
	the number of passes vs fails."""
	def __init__(self, webSite, package_generator, numberOfRuns, success=None, fail=None, waitTime=None):
		threading.Thread.__init__(self)
		self.webSite = webSite
		self.package_generator = package_generator
		self.numberOfRuns = numberOfRuns
		self.averageRun = None
		self.hits =[]
		self.begTime = None
		self.totalRunTime = None 
		self.success = success
		self.fail = fail
		self.report = {}
		self.running = True
		self.waitTime = waitTime

	def run(self):
		for i in range(self.numberOfRuns):
			temp_case = self.package_generator.gen_case()
			self.hits.append(hit(self.webSite, temp_case["input"], {"key":temp_case["key"],"value":temp_case["output"]}, self.fail))
		self.begTime = datetime.datetime.now()
		print "starting trashing"
		for h in self.hits:
			h.start()
		for h in self.hits:
			h.join()
		self.totalRunTime = datetime.datetime.now() - self.begTime
		tSum = self.begTime - self.begTime
		suc = 0
		fails = 0
		print "thrashing finished"
		for h in self.hits:
			tSum = tSum + h.timeSpent
			if h.pas:
				suc = suc + 1
			else:
				fails = fails + 1
		ave = tSum/self.numberOfRuns
		self.report["ave"] = ave
		self.report["NumOfSuc"] = suc
		self.report["NumOfFails"] = fails
		self.report["totalTime"] = tSum
		self.report["realTime"] = self.totalRunTime

if __name__ == "__main__":
	ws = "http://127.0.0.1:9000/stressTest"
	da = ball()
	su = None
	su = "task"
	nu = 10000
	t = thrasher(ws, da, nu, su)
	t.start()
	t.join()
	print t.report
