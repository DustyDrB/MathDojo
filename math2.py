class MathDojo(object):
	def __init__(self):
		self.result = 0
		print "Let's do math!"
	def add(self, *nums):
		for item in nums:
			if type(item) is list:
				for num in item:
					self.result += num
			else:
				self.result += item
		return self
	def subtract(self, *nums):
		for item in nums:
			if type(item) is list:
				for num in item:
					self.result -= num
			else:
				self.result -= item
		return self

md = MathDojo()

print md.add([1],3,4).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, [2,3], [1.1, 2.3]).result