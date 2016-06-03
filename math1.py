class MathDojo(object):
	def __init__(self):
		self.result = 0
		self.sum = 0
		self.sub = 0
		print "Let's do math!"
	def add(self, *nums):
		if type(nums) is tuple:
			for num in nums:
				self.result += num
		return self
	def subtract(self, *nums):
		if type(nums) is tuple:
			for num in nums:
				self.result -= num
		return self

md = MathDojo()

print md.add(2).add(2, 5).subtract(3, 2).result
