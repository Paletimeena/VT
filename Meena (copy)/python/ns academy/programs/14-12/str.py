class Animal(object):
	def __init__(self,name):
		self.name=name
	def __str__(self):
	        return self.name
animal=Animal('cat')
print animal
