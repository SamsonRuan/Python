#创建一个地瓜类
class SweetPotato:
	def __init__(self):
		self.cooked_level = 0
		self.cooked_statue = "生的"
		self.condiments = []
	def __str__(self):
		return "%s(%d) %s"%(self.cooked_statue,self.cooked_level,str(self.condiments))
	def roast_sweetpoato(self,cook_time):
		self.cooked_level += cook_time
		if self.cooked_level >=0 and self.cooked_level<=3:
			self.cooked_statue = "生的"
		elif self.cooked_level >3 and self.cooked_level<=5:
			self.cooked_statue = "半生不熟的"
		elif self.cooked_level >5 and self.cooked_level<=8:
			self.cooked_statue = "熟的"
		else:
			self.cooked_statue = "烤糊了"
	def add_condiment(self,condiment):
		self.condiments.append(condiment)
		
sweet_poato = SweetPotato()

sweet_poato.roast_sweetpoato(1)
sweet_poato.add_condiment("盐")
print(sweet_poato)
sweet_poato.roast_sweetpoato(1)
sweet_poato.add_condiment("胡椒")
print(sweet_poato)
sweet_poato.roast_sweetpoato(1)
sweet_poato.add_condiment("八角")
print(sweet_poato)
sweet_poato.roast_sweetpoato(1)
sweet_poato.roast_sweetpoato(1)
sweet_poato.roast_sweetpoato(1)
print(sweet_poato)