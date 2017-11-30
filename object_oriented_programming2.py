class Dog:
	def set_age(self,age):
		self.age = age
	def set_name(self,name):
		self.name = name
	def get_age(self):
		 print(self.age )
	def get_name(self):
		print(self.name)
	def run(self):
		print("%s can run..."%self.name)
	#init方法类似于构造函数，由系统自动调用，用于对类属性进行初始化设置
	#也可以用set方法对类属性进行初始化设置
	def __init__(self,color):
		self.color = color
	def __str__(self):
		return "the color of %s is %s"%(self.name,self.color)

tom = Dog("grey")
tom.set_age(18)
tom.set_name("Tom")
tom.get_age()
tom.get_name()
print(tom)

	