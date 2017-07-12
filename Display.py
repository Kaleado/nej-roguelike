import libtcodpy as libtcod


# Takes a 2d aray and a starting x and y position, and draws the array on the map.
# Arrays are organised as such:
#
# [ , , , , , , , ... ]    
# [ , , , , , , , ... ]    ^
#         ....             | Y axis
# [ , , , , , , , ... ]    V
# [ , , , , , , , ... ]
#        <---> x axis
#
#     accessed like this:
#      map[x][y]
def draw(startx, starty, data):
	# Case for single char
	if type(data) is str:
		putch(data[0], startx, starty)
	else:
		# Case for 2d array
		for i in range(0, len(data)):
			for j in range(0, len(data[i])):
				putch(data[i][j], startx + i, starty + j)

def putch(obj, x, y):
	# If a string, print the first character and white, the default
	if isinstance(obj, basestring):
		libtcod.console_set_default_foreground(0, libtcod.white)
		libtcod.console_put_char(0, x, y, obj[0], libtcod.BKGND_NONE)
	# Otherwise, print the objects character and it's designated color
	else:
		libtcod.console_set_default_foreground(0, obj.color())
		libtcod.console_put_char(0, x, y, obj.char(), libtcod.BKGND_NONE)
			
