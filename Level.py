import libtcodpy as libtcod
import random
import Display

class Tile:
    def __init__(self, character, passable, blocksSight, color=libtcod.white):
        self._character = character
        self._passable = passable
        self._blocksSight = blocksSight
        self._color = color
    def isPassable(self):
        return self._passable
    def blocksSight(self):
        return self._blocksSight
    def showAt(self, x, y):
        libtcod.console_put_char(0, x, y, self._character, libtcod.BKGND_NONE)
    def color(self):
        return self._color
    def char(self):
        return self._character

class Level:
    def __init__(self, width, height):
        self._width = width
        self._height = height
        self._terrain = [[ None for y in range(height) ] for x in range(width)]
        self._creatures = []
        self._items = []
    def generate(self):
        for x in range(self._width):
            for y in range(self._height):
                if random.randint(0, 3) != 0:
                    self._terrain[x][y] = Tile('.', True, False)
                else:
                    self._terrain[x][y] = Tile('#', False, True)
    def show(self):
        Display.draw(0,0,self._terrain)
        """for x in range(self._width):
            for y in range(self._height):
                if self._terrain[x][y] is not None:
                    self._terrain[x][y].showAt(x, y)"""
    def getTile(self, x, y):
        return self._terrain[x][y]
    def getCreatureAt(self, x, y):
        for c in self._creatures:
            if c is not None and c.x == x and c.y == y:
                return c
        return None
    def getItemAt(self, x, y):
        for c in self._items:
            if c is not None and c.x == x and c.y == y:
                return c
        return None
    def removeItem(self, item):
        self._items.remove(item)
    def removeItem(self, creature):
        self._creatures.remove(creature)

currentLevel = Level(80, 50)
currentLevel.generate()
