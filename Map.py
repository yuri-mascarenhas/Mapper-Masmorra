from PPlay.gameimage import *
from PPlay.sprite import *

class Map(object):
    """
    Define o Mapa a ser construído/salvo
    """
    #--------------------Atributos--------------------
    _map = []
    _lines = 0
    _columns = 0

    #--------------------Métodos--------------------
    def __init__(self, lines, columns):
        self._lines = lines
        self._columns = columns
        for i in range(lines):
            self._map.append([])
            for j in range(columns):
                self._map[i].append(Sprite("null.png"))
        self.position_tiles()
   
    """Getters e Setters"""
    def get_line_len(self):
        return self._lines

    def get_column_len(self):
        return self._columns

    def get_tile(self, line, column):
        return self._map[line][column]

    def set_tile(self, sprite, line, column):
        self._map[line][column] = sprite

    """Posiciona as Sprites de cada elemento da matriz-mapa"""
    def position_tiles(self):
        for i in range(self._lines):
            for j in range(self._columns):
                self._map[i][j].x = j * 48
                self._map[i][j].y = i * 48

    def draw(self):
        for i in range(self._lines):
            for j in range(self._columns):
                self._map[i][j].draw()

    def save_map(self, name):
        file = open(name, 'w')
        for i in range(self._lines):
            for j in range(self._columns):
                file.write(self._map[i][j] + '\n')