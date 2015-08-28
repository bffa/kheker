import requests
import json
import threading
import datetime


class hit(threading.Thread):
	"""A thread to hit the web sit with. Keeps track of the time required for server
	to respont.
	@webSite: the site being tested,
	@package: the jsone being sent to site,
	@success: a json object with these items in it
		{'key':(a key word to expect in the returned json),
		 'value: (expected value associated with the key)'},
	@fail: a json with these items in it
		{'key':(a key word to expect in the returned json),
		 'value: (expected value associated with the key)'},
	@waitTime: currently not implemented, however ment to be the amount of time the thread should wait."""
	def __init__(self, webSite, package, success=False, fail=False, waitTime=None):
		threading.Thread.__init__(self)
		self.webSite = webSite
		self.running = True
		self.begTime = None
		self.package = package
		self.success = success
		self.fail = fail
		self.pas = False
		self.timeSpent = None
		self.running = True
		self.waitTime = waitTime
	
	def run(self):
		try:
			rec = {"val": self.package}
			self.begTime = datetime.datetime.now()
			r = requests.get(self.webSite, data = json.dumps(rec))
			self.timeSpent =datetime.datetime.now() - self.begTime
			if self.success or self.fail:
				try:
					j = r.text.replace("'", "\"")
					js = json.loads(j.encode('ascii','ignore'))
					if self.success and (self.success["key"] in js):
						self.pas = (self.success["value"] == js[self.success["key"]])
						
					if self.fail and (self.fail.key in js):
						if (not js[fail]):
							self.pas = True
							
				except:
					print "a run failed to parse correctly"
			else:
				if r.status_code == 200:
					self.pas = True
				else:
					print r.status_code
			#print r
			self.running = False
			
		except:
			print "failed to run test"



	def passed(self):
		return self.pas

if __name__ == "__main__":
	WS = "http://127.0.0.1:9000/stressTest"
	package = {"temp":"tester"}
	su = "task"
	h = hit(WS, package, su)
	h.start()
	print h.running
	print "waiting for a join"
	h.join()
	print "after join"
	print h.running
	print h.timeSpent
	print h.pas

r = requests.get("https://www.youtube.com/")
