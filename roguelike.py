import libtcodpy as libtcod
import Level
from Character import Character
import Display

#actual size of the window
SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50

LIMIT_FPS = 20  #20 frames-per-second maximum

def handle_move(entity, dx, dy):
    if Level.currentLevel.getTile(entity.x + dx, entity.y + dy).isPassable():
        if Level.currentLevel.getCreatureAt(entity.x + dx, entity.y + dy) == None:
            entity.move(dx,dy)
        else:
            entity.attack(dx, dy)
    else:
        pass


def handle_keys():
    key = libtcod.console_wait_for_keypress(True)  #turn-based
    if key.vk == libtcod.KEY_ENTER and key.lalt:
        #Alt+Enter: toggle fullscreen
        libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())
    elif key.vk == libtcod.KEY_ESCAPE:
        return True  #exit game

    #movement keys
    if libtcod.console_is_key_pressed(libtcod.KEY_UP):
        handle_move(player, 0, -1)
    elif libtcod.console_is_key_pressed(libtcod.KEY_DOWN):
        handle_move(player, 0, 1)
    elif libtcod.console_is_key_pressed(libtcod.KEY_LEFT):
        handle_move(player, -1, 0)
    elif libtcod.console_is_key_pressed(libtcod.KEY_RIGHT):
        handle_move(player, 1, 0)

    # Player interaction
    if key.vk == libtcod.KEY_CHAR:
        if key.c == ord('g'):
            item = Level.currentLevel.getItemAt(player.x, player.y)
            if item != None:
                player.pickup(item)
                # Level.item.destroy() ??

#############################################
# Initialization & Main Loop
#############################################
 
libtcod.console_set_custom_font('terminal10x10_gs_tc.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'python/libtcod tutorial', False)
libtcod.sys_set_fps(LIMIT_FPS)

# Create our player character and set their position, items, char, etc.
player = Character('@', [], SCREEN_WIDTH/2, SCREEN_HEIGHT/2, None)

while not libtcod.console_is_window_closed():
    Level.currentLevel.show()
    libtcod.console_set_default_foreground(0, libtcod.red)
    libtcod.console_put_char(0, player.x, player.y, player.char(), libtcod.BKGND_NONE)
    libtcod.console_set_default_foreground(0, libtcod.white)

    test = [ ['%','%','%','%','%','%'],
         	 ['%','%','%','%','%','%'],
         	 ['%','%','%','%','%','%'],
         	 ['%','%','%','%','%','%'] ]

    Display.draw(0,0,test)

    libtcod.console_flush()
    libtcod.console_put_char(0, player.x, player.y, ' ', libtcod.BKGND_NONE)
    
    
    #handle keys and exit game if needed
    exit = handle_keys()
    if exit:
        break
