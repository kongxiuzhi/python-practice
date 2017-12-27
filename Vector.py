class Vector:
	"""Represent a vector in multidimensional sapce"""
	def __init__(self,d):

		self._coodrs =[0] *d #create d-dimensional vector of zeros

	def __len__(self):

		return len(self._coodrs)

	def __getitem__(self,j):

		return self._coodrs[j]

	def __setitem__(self,j,value):

		self._coodrs[j] = value

	def __add__(self,other):

		if len(self)!=len(other):
			raise ValueError('dimensional must agree')
		result = Vector(len(self))
		for j in range(len(self)):
			result[j] = self[j] + other[j]
		return result

	def __eq__(self,other):
		return self._coodrs == other._coodrs
	def __ne__(self,other):
		return not self==other
	def __str__(self):
		return '<' + str(self._coodrs)[1:-1] + '>'

if __name__ == "__main__":
	v1 = Vector(5)
	v2 = Vector(5)
	v1[1] = 1
	v2[2] = 1
	v3 = v1 + v2
	print(v3)