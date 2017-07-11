import libtcodpy as libtcod
import Level

class Character:	
	#strength, agility, maxhp and hp
	_str = 0
	_agl = 0
	hp = 10
	_maxhp = 10
	

	# Requires a playes character and initial items
	def __init__(self, char='@', items=[], y=0, x=0, stats=None):
		self.char = char
		self.items = []
		self.y = y
		self.x = x
		
		if stats != None:
			try:
				self._maxhp = stats["maxhp"]
				self._hp = self._maxhp
				self._str = stats["str"]
				slef._agl = stats["agl"]
			except KeyError:
				if not self._maxhp:
					self._maxhp = 10
				if not self._str:
					self._str = 10
				if not self._agl:
					self._agl = 10
		                        
			

	#puts player char in place
	def showat(self):
    	        libtcod.console_put_char(0, self.x, self.y, self.char, libtcod.BKGND_NONE)

	# A delta for moving left/right x amount, and up/down y amount
	def move(x, y):
		if Level.getcreatureatxy(self.x + x, self.y + y) != None:
			self.attack(self.x + x, self.y + y)
		else:
			self.y += y
			self.x += x

	def attack(x, y):
		pass
