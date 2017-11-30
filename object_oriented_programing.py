#创建一个类
class Cat:
	#类中的函数必须在形式参数的第一位加self，相当于对象实例自身的引用，相当于this
	def eat(self):
		print("I'm eatting...")
	def drink(self):
		print("%s is drinking..."%self.name)
	def introduce(self):
		print("I'm %s,I come from %s"%(self.name,self.addr))
#创建一个对象实例
tom=Cat()
#为这个对象实例添加属性
tom.name="Tom"
tom.addr="Village"
#调用这个对象中的方法
tom.eat()
tom.drink()
tom.introduce()