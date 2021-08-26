from data.tile import *
from data.PPlay.gameimage import *
from data.PPlay.sprite import *
from copy import copy

class Menu(object):
    """
    Define o layout e as funcionalidades do menu da aplicação Mapper,
    onde os principais aspectos são os botões (atributo _buttons) e os
    tiles que podem ser usados para construir o mapa (atributo canvas).
    """
    #--------------------Atributos--------------------
    _buttons: list[Sprite] = []
    canvas: Tileset = []

    _background: GameImage
    
    #--------------------Métodos--------------------
    def __init__(self, tileset, default_background="resources/background/menu.png"):
        self._buttons = [Sprite("resources/buttons/clear.png"), Sprite("resources/buttons/save.png")]

        self._background = GameImage(default_background)
        self._background.y = 600

        for i in range(len(tileset)): 
            self.canvas.append(copy(tileset[i]))
        for i in range(len(self._buttons)):
            self._buttons[i].x = 736
            self._buttons[i].y = 616 + (i * 36)
        for i in range(0, len(self.canvas), 3):
            for j in range(3):
                if(i + j < len(self.canvas)):
                    self.canvas[i + j].x = 16 + ((i / 3) * 64)
                    self.canvas[i + j].y = 616 + (j * 64)

    """Retorna o número de botões do Menu"""
    def get_buttons_len(self):
        return len(self._buttons)

    """Retorna a lista que contém os botões"""
    def get_buttons(self):
        return self._buttons

    def draw(self):
        self._background.draw()
        for i in range(len(self._buttons)):
            self._buttons[i].draw()
        for i in range(0, len(self.canvas), 2):
            for j in range(2):
                if(i + j < len(self.canvas)):
                    self.canvas[i + j].draw()
