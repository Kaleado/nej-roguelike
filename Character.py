import libtcodpy as libtcod
from Level import Level

class Character:	
	#strength, agility, maxhp and hp
	_str = 0
	_agl = 0
	_maxhp = 10
	hp = 10
	
	# Requires a playes character and initial items
	def __init__(self, char='@', items=[], y=0, x=0, stats=None, color=libtcod.red):
		self._char = char
		self.items = []
		self.y = y
		self.x = x
		self._color = libtcod.red
		
		if stats != None:
			try:
				self._maxhp = stats["maxhp"]
				self._hp = self._maxhp
				self._str = stats["str"]
				slef._agl = stats["agl"]
			except KeyError:
				if self._maxhp is None:
					self._maxhp = 10
				if self._str is None:
					self._str = 10
				if self._agl is None:
					self._agl = 10

	#puts player char in place
	def showat(self):
		libtcod.console_put_char(0, self.x, self.y, self.char, libtcod.BKGND_NONE)

	# A delta for moving left/right x amount, and up/down y amount
	def move(self, x, y):
		self.y += y
		self.x += x

	def attack(self, x, y):
		pass
	def char(self):
		return self._char
	def color(self):
		return self._color
