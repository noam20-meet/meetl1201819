'''
class Animal(object):
	def __init__(self,sound,name,age,favorite_color):
		self.sound = sound 
		self.name = name
		self.age = age
		self.favorite_color = favorite_color
	def eat(self,food):
		print("Yummy!!! " + self.name + " is eating " + food)
	def description(self):
		print(self.name + " is "+  self.age + " years old and loves the color " + self.favorite_color)
	#def make_sound(self):	
		#print(self.sound*3)	

#n= Animal("woof", "Nevi" , "12" , "Blue")
#n.eat("bonzo")
#n.description()

'''


class Person(object):
	def __init__ (self,name,age,city,gender,breakfast):
		self.name = name
		self.age = age
		self.city = city
		self.gender = gender
		self.breakfast=breakfast
	def eat_breakfast(self):
		print(self.name +" is eating " + self.breakfast)
z= Person("Zohar" , "15", "Jerusalem", "feamle", "chocolate")		
		
z.eat_breakfast()
