class Car: # define the class with a name 
	
	
	def __init__(self, name, wheels=4): #self==c, define a method
		self.name = name	# assigns a property to the instance
		self.wheels = wheels
	def __str__(self):
		"""
		give the instance a name. Is called during 'print(intsance)'
		"""		
		return "{0} wiht {1} wheels".format(self.name, self.wheels)

	
	i = 'alo'
i = Car('Wagon') #make an object from class, ie Instantiation
print(i) #when print a instance, the __str__method is called
#c.print_wheels()

#test
#test2
