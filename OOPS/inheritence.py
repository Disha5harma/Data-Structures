class Vehicle:

	def __init__(self,color,maxSpeed):
		self.color = color
		self.maxSpeed = maxSpeed

class Car(Vehicle):

	def __init__(self,color,maxSpeed,numGears,isConvertible):

		super().__init__(color,maxSpeed)
		self.numGears = numGears
		self.isConvertible = isConvertible

	def printCar(self):
		print("Color :" ,self.color)
		print("MaxSpeed :",self.maxSpeed)
		print("NumGears :",self.numGears)
		print("IsConvertible :", self.isConvertible)


c = Car("red",15,3,False)
c.printCar()

#INHERITENCE AND PRIVATE VARIABLES

class Vehicle:

	def __init__(self,color,maxSpeed):
		self.color = color
		self.__maxSpeed = maxSpeed

	def getMaxSpeed(self):
		return self.__maxSpeed

	def setMaxSpeed(self,maxSpeed):
		self.__maxSpeed = maxSpeed

	def print(self):
		print("Color :" ,self.color)
		print("MaxSpeed :",self.__maxSpeed)

class Car(Vehicle):

	def __init__(self,color,maxSpeed,numGears,isConvertible):

		super().__init__(color,maxSpeed)
		self.numGears = numGears
		self.isConvertible = isConvertible

	def printCar(self):
		self.print()
		print("NumGears :",self.numGears)
		print("IsConvertible :", self.isConvertible)


c = Car("red",15,3,False)
c.printCar()

#INHERITENCE AND POLYMORPHISM

class Vehicle:

	def __init__(self,color,maxSpeed):
		self.color = color
		self._maxSpeed = maxSpeed

	@classmethod
	def getMaxSpeed(cls):
		return 15

	def setMaxSpeed(self,maxSpeed):
		self._maxSpeed = maxSpeed

	def print(self):
		print("Color :" ,self.color)
		print("MaxSpeed :",self._maxSpeed)

class Car(Vehicle):

	def __init__(self,color,maxSpeed,numGears,isConvertible):

		super().__init__(color,maxSpeed)
		self.numGears = numGears
		self.isConvertible = isConvertible

	def print(self):
		# super().print()
		print("Color :" ,self.color)
		print("MaxSpeed :",self._maxSpeed)
		print("NumGears :",self.numGears)
		print("IsConvertible :", self.isConvertible)


# c = Car("red",15,3,False)
# c.print()
#print()
v = Vehicle("red",18)
v.print()
print()
v._maxSpeed = 19
get = v.getMaxSpeed()
print(get)

#PROTECTED MEMBERS

class Vehicle:

	def __init__(self,color,maxSpeed):
		self.color = color
		self._maxSpeed = maxSpeed

	@classmethod
	def getMaxSpeed(cls):
		return 15

	def setMaxSpeed(self,maxSpeed):
		self._maxSpeed = maxSpeed

	def print(self):
		print("Color :" ,self.color)
		print("MaxSpeed :",self._maxSpeed)

class Car(Vehicle):

	def __init__(self,color,maxSpeed,numGears,isConvertible):

		super().__init__(color,maxSpeed)
		self.numGears = numGears
		self.isConvertible = isConvertible

	def print(self):
		# super().print()
		print("Color :" ,self.color)
		print("MaxSpeed :",self._maxSpeed)
		print("NumGears :",self.numGears)
		print("IsConvertible :", self.isConvertible)


# c = Car("red",15,3,False)
# c.print()
#print()
v = Vehicle("red",18)
v.print()
print()
v._maxSpeed = 19
get = v.getMaxSpeed()
print(get)

#MULTIPLE INHERITENCE

class Mother:

	def __init__(self):
		self.name = "Manju"
		super().__init__()

	def print(self):

		print("Print Of Mother called")

class Father:

	def __init__(self):
		self.name = "Ajay"
		super().__init__()
	def print(self):

		print("Print Of Father called")

class Child(Mother,Father):

	def __init__(self):
		super().__init__()

	def print(self):
		print("Name of child is", self.name)

c = Child()
c.print()
print(Child.mro())

#OPERATOR OVERLOADING


import math
class Point:

	def __init__(self,x,y):
		self.__x = x
		self.__y = y


	def __str__(self):

		return "This point is at (" + str(self.__x) + "," + str(self.__y) + ")"

	def __add__(self,point_object):
		return Point(self.__x + point_object.__x,self.__y + point_object.__y)

	def __lt__(self,point_object):
		return math.sqrt(self.__x**2 + self.__y**2) < math.sqrt(point_object.__x**2 + point_object.__y**2)


p1 = Point(1,2)
p2 = Point(3,4)
p3 = p1 + p2
print(p3)
print(p2<p1)