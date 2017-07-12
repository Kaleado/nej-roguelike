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

def putch(char, x, y):
	# Check if the dict of colours exists
	if 'colors' in locals():
		# Print found color, otherwise white
		if char in colors:
			libtcod.console_set_default_foreground(0, colors[char])
			libtcod.console_put_char(0, x, y, char, libtcod.BKGND_NONE)
			libtcod.console_set_default_foreground(0, libtcod.white)
		else:
			libtcod.console_set_default_foreground(0, libtcod.white)
			libtcod.console_put_char(0, x, y, char, libtcod.BKGND_NONE)
			
