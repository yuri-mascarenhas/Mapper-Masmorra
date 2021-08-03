import copy
from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from Map import *
from Menu import *

#--------------------Elementos Base do Jogo--------------------
window = Window(800, 800)
keyboard = Window.get_keyboard()
mouse = Window.get_mouse()
window.set_title("Mapper")

bg = GameImage("bg.png")
bg2 = GameImage("bg2.png")
bg2.y = 600

over = Sprite("mouse_over.png")
selected = Sprite("assets/tiles/chao0.png")
selected_id = 0

new_map = Map(13, 17)
menu = Menu()

#-------------------------Game Loop-------------------------
while(not keyboard.key_pressed("ESC")):
    # Entrada de dados
    
    # Update dos Game Objects
    """Seleciona qual tile será utilizado"""
    for i in range(len(menu.get_canvas())):
        if(mouse.is_over_object(menu.get_canvas()[i]) and mouse.is_button_pressed(1)):
            selected = copy.copy(menu.get_canvas()[i])
            selected_id = i
    
    """Seleciona um dos botões do menu"""
    for i in range(len(menu.get_buttons())):
        if(mouse.is_over_object(menu.get_buttons()[i]) and mouse.is_button_pressed(1)):
            if(i == 0):
                new_map.clear()
            if(i == 1):
                new_map.save("maps/teste.txt")

    """Salva no mapa o tile desejado"""
    for i in range(new_map.get_line_len()):
        for j in range(new_map.get_column_len()):
            if(mouse.is_over_object(new_map.get_tile(i, j)) and mouse.is_button_pressed(1)):
                new_map.set_tile(copy.copy(selected), selected_id, i, j)                

    # Draw dos Game Objects
    """Draw das partes do mapa (y < 600)"""
    bg.draw()
    new_map.draw()
    for i in range(new_map.get_line_len()):
        for j in range(new_map.get_column_len()):
            if(mouse.is_over_object(new_map.get_tile(i, j))):
                selected.x = new_map.get_tile(i, j).x
                selected.y = new_map.get_tile(i, j).y
                selected.draw()

    """Draw das partes do menu (y > 600)"""
    bg2.draw()
    menu.draw()
    for i in range(len(menu.get_canvas())):
        if(mouse.is_over_object(menu.get_canvas()[i])):
            over.x = menu.get_canvas()[i].x
            over.y = menu.get_canvas()[i].y
            over.draw()
    
    window.update()