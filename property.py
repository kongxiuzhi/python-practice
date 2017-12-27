class Person:
	def __init__(self,name):
		self._name = name 
	def getName(self):
		print('fetch...')
		return self._name
	def setName(self,value):
		print('change...')
		self._name = value
	def delName(self):
		print('remove...')
		del self._name
	name = property(getName,setName,delName,"name property docs")

class Person1:
	def __init__(self,name):
		self._name = name

	@property
	def name(self):
		return self._name 
#	@name.setter			#readonly
#	def name(self,value):
#		self._name = value
	@name.deleter
	def name(self):
		del self._name 
#描述符
"""
class Descriptor:
#	""docstring goes here""

	def __get__(self,instance,owner):
	def __set__(self,instance,value):
	def __delete(self,instance):
self 描述符类实例，instance 描述符实例所附加的类的实例，owner附加的类
"""
class Name:
	"name descriptor docs"
	def __get__(self,instance,owner):
		print("fetch...")
		return instance._name
	def __set__(self, instance, value):
		print("change...")
		instance._name=value
	def __delete__(self, instance):
		print('remove..')
		del instance._name

class Person2:
	def __init__(self,name):
		self._name = name
	name = Name()

#compute
class DescSquare:
	def __init__(self,start):
		self.value = start
	def __get__(self, instance, owner):
		return self.value**2
	def __set__(self, instance, value):
		self.value=value
class Client1:
	X=DescSquare(3)
class Client2:
	X=DescSquare(32)

class Property:
	def __init__(self,fget=None,fset=None,fdel=None,doc=None):
		self.fget = fget
		self.fset = fset
		self.fdel = fdel
		self.__doc__=doc
	def __get__(self, instance, owner):
		if instance is None:
			return self
		if self.fget in None:
			raise AttributeError("can't get attribute")
		return self.fget(instance)
	def __set__(self, instance, value):
		if self.fset is None:
			raise AttributeError("can't set attribute")
		self.fset(instance)
	def __delete__(self, instance):
		if self.fdel in None:
			raise AttributeError("can't delete attribute")
		self.fdel(instance)




if __name__ =="__main__":
	bob = Person1('bob Smith')
	print(bob.name)
	#bob.name = "Robert Smith"
	print(bob.name)
	print(Person.name.__doc__)
	del bob.name
	p1 = Person2("Jone")
	print(p1.name)
	p1.name="Jone snow"
	del p1.name
	c1=Client1()
	c2=Client2()
	print(c1.X)
	c1.X = 4
	print(c1.X)
	print(c2.X)