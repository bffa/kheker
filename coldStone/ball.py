from package_generator import package_generator

class ball(package_generator):
	"""a simple incrementer generator.
	Generates numbers in an incrementing patern"""

	def __init__(self):
		package_generator.__init__(self, "ball")
		self.next_value = 1

	def gen_case(self):
		v = {"input": self.next_value, "output": self.next_value+1, "key":"received"}
		self.next_value = self.next_value + 1
		return v

if __name__ == "__main__":
	b = ball()
	print b.get_type()
	for i in range(9):
		print b.gen_case();
