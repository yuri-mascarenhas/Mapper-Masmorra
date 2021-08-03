from PPlay.gameimage import *
from PPlay.sprite import *

class Menu(object):
    """
    Define o layout e as funcionalidades do menu da aplicação Mapper,
    onde os principais aspectos são os botões (atributo _buttons) e os
    tiles que podem ser usados para construir o mapa (atributo _canvas).
    """
    #--------------------Atributos--------------------
    _buttons = []
    _canvas = []
    
    #--------------------Métodos--------------------
    def __init__(self):
        self._buttons = [Sprite("assets/buttons/clear.png"),        
                         Sprite("assets/buttons/save.png")]
        self._canvas = [Sprite("assets/tiles/chao0.png"),
                        Sprite("assets/tiles/paredeCID.png"),
                        Sprite("assets/tiles/paredeCIE.png"),
                        Sprite("assets/tiles/paredeCSD.png"),
                        Sprite("assets/tiles/paredeCSE.png"),
                        Sprite("assets/tiles/paredeMI.png"),
                        Sprite("assets/tiles/paredeMS.png"),
                        Sprite("assets/tiles/paredeTriID.png"),
                        Sprite("assets/tiles/paredeTriIE.png"),
                        Sprite("assets/tiles/paredeTriSD.png"),
                        Sprite("assets/tiles/paredeTriSE.png"),
                        Sprite("assets/tiles/paredeE.png"),
                        Sprite("assets/tiles/paredeD.png"),]
        self.position_elements()
   
    """Define onde cada opção de botão e tile para uso do usuário ficará na tela"""
    def position_elements(self):
        for i in range(len(self._buttons)):
            self._buttons[i].x = 736
            self._buttons[i].y = 616 + (i * 36)
        for i in range(0, len(self._canvas), 3):
            for j in range(3):
                if(i + j < len(self._canvas)):
                    self._canvas[i + j].x = 16 + (i * 32)
                    self._canvas[i + j].y = 616 + (j * 64)
    
    """Retorna a lista que contém o canvas"""
    def get_canvas(self):
        return self._canvas

    """Retorna a lista que contém os botões"""
    def get_buttons(self):
        return self._buttons

    def draw(self):
        for spr in self._buttons:
            spr.draw()
        for spr in self._canvas:
            spr.draw()