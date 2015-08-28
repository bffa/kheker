class package_generator(object):
	"""generates both an input for a test, 
	and an expected output for the test. This class 
	is supposed to be an abstract class, or an 
	interface."""

	def __init__(self, type_gen):
		self.type_gen = type_gen

	def get_type(self):
		return self.type_gen

	def gen_case(self):
		v = {"input": 1, "output": 1, "key":"received"}
		return v

if __name__ == "__main__":
	pg = package_generator("sample")
	print pg.gen_case()