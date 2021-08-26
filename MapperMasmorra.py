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

wall_tileset = Tileset([
    Tile("resources/tiles/floor/floor_1.png", 1, 0),
    Tile("resources/tiles/floor/floor_2.png", 1, 0),
    Tile("resources/tiles/floor/floor_3.png", 1, 0),
    Tile("resources/tiles/wall/wall_corner_bottom_left.png", 1, 2),
    Tile("resources/tiles/wall/wall_corner_bottom_right.png", 1, 2),
    Tile("resources/tiles/wall/wall_corner_front_left.png", 1, 2),
    Tile("resources/tiles/wall/wall_corner_front_right.png", 1, 2),
    Tile("resources/tiles/wall/wall_corner_left.png", 1, 2),
    Tile("resources/tiles/wall/wall_corner_right.png", 1, 2),
    Tile("resources/tiles/wall/wall_corner_top_left.png", 1, 2),
    Tile("resources/tiles/wall/wall_corner_top_right.png", 1, 2),
    Tile("resources/tiles/wall/wall_fountain_top.png", 1, 2),
    Tile("resources/tiles/wall/wall_hole_1.png", 1, 2),
    Tile("resources/tiles/wall/wall_hole_2.png", 1, 2),
    Tile("resources/tiles/wall/wall_inner_corner_l_top_left.png", 1, 2),
    Tile("resources/tiles/wall/wall_inner_corner_l_top_rigth.png", 1, 2),
    Tile("resources/tiles/wall/wall_inner_corner_mid_left.png", 1, 2),
    Tile("resources/tiles/wall/wall_inner_corner_mid_rigth.png", 1, 2),
    Tile("resources/tiles/wall/wall_inner_corner_t_top_left.png", 1, 2),
    Tile("resources/tiles/wall/wall_inner_corner_t_top_rigth.png", 1, 2),
    Tile("resources/tiles/wall/wall_left.png", 1, 2),
    Tile("resources/tiles/wall/wall_mid.png", 1, 2),
    Tile("resources/tiles/wall/wall_right.png", 1, 2),
    Tile("resources/tiles/wall/wall_side_front_left.png", 1, 2),
    Tile("resources/tiles/wall/wall_side_front_right.png", 1, 2),
    Tile("resources/tiles/wall/wall_side_mid_left.png", 1, 2),
    Tile("resources/tiles/wall/wall_side_mid_right.png", 1, 2),
    Tile("resources/tiles/wall/wall_side_top_left.png", 1, 2),
    Tile("resources/tiles/wall/wall_side_top_right.png", 1, 2),
    Tile("resources/tiles/wall/wall_top_left.png", 1, 2),
    Tile("resources/tiles/wall/wall_top_mid.png", 1, 2),
    Tile("resources/tiles/wall/wall_top_right.png", 1, 2)
    ])
tilesets = {"wall": wall_tileset}

map = Map(800, 600, 48, 48, 3)
wall_menu = Menu(wall_tileset)
menu = {"wall": wall_menu}
mode = "wall"
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

    menu[mode].draw()
    for i in range(len(menu[mode].canvas)):
        if(mouse.is_over_object(menu[mode].canvas[i])):
            over.x = menu[mode].canvas[i].x
            over.y = menu[mode].canvas[i].y
            over.draw()
            if(mouse.is_button_pressed(1)):
                selected = tilesets[mode][i]
                selected_id = i
    
    if(mouse.is_over_object(menu[mode].get_buttons()[0]) and mouse.is_button_pressed(1)):
        map.clear()
    if(mouse.is_over_object(menu[mode].get_buttons()[1]) and mouse.is_button_pressed(1)):
        map.save()

    window.update()