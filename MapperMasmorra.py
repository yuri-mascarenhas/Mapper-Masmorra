from data.map import *
from data.PPlay.window import *
from data.PPlay.gameimage import *
from data.PPlay.sprite import *
from data.tile import *
from data.menu import *

#--------------------Elementos Base do Jogo--------------------
window = Window(800, 800)
mouse = Window.get_mouse()
keyboard = Window.get_keyboard()

tileset = Tileset([ 
    Tile("resources/tiles/floor_1.png", 1, 0),
    Tile("resources/tiles/floor_2.png", 1, 0),
    Tile("resources/tiles/floor_3.png", 1, 0),
    Tile("resources/chest/1x3chest.png", 3, 1),
    Tile("resources/tiles/wall_side_mid_left.png", 1, 2),
    Tile("resources/tiles/wall_side_mid_right.png", 1, 2)
])

map = Map(800, 600, 48, 48, tileset.layers)
menu = Menu(tileset)
over = Sprite("resources/mouse_over.png")

selected = None
selected_id = -1

window.set_background_color((0,0,0))
window.set_title("Mapper")

while(not keyboard.key_pressed("ESC")):
    map.draw()
    for x in range(map.lines):
        for y in range(map.columns):
            if(mouse.is_over_object(map.get_tile(0, x, y)) and selected):
                selected.draw_at(map.get_tile(0, x, y).x, map.get_tile(0, x, y).y)
                if(mouse.is_button_pressed(1)):
                    map.set_tile(selected, selected.layer, x, y)
                if(mouse.is_button_pressed(3)):
                    map.delete_tile(selected.layer, x, y)

    menu.draw()
    for i in range(len(menu.canvas)):
        if(mouse.is_over_object(menu.canvas[i])):
            over.x = menu.canvas[i].x
            over.y = menu.canvas[i].y
            over.draw()
            if(mouse.is_button_pressed(1)):
                selected = tileset[i]
                selected_id = i
    
    if(mouse.is_over_object(menu.get_buttons()[0]) and mouse.is_button_pressed(1)):
        map.clear()
    if(mouse.is_over_object(menu.get_buttons()[1]) and mouse.is_button_pressed(1)):
        map.save()

    window.update()