from PPlay.gameimage import *
from PPlay.sprite import *

class Map(object):
    """
    Define o Mapa a ser construído/salvo
    """
    #--------------------Atributos--------------------
    _map = []
    _map_save = []                # Lista que guarda os códigos de cada tile em sua posição para ser salvo
    _lines = 0
    _columns = 0

    #--------------------Métodos--------------------
    def __init__(self, lines, columns):
        self._lines = lines
        self._columns = columns
        for i in range(lines):
            self._map.append([])
            self._map_save.append([])
            for j in range(columns):
                self._map[i].append(Sprite("null.png"))
                self._map_save[i].append(-1)
        self.position_tiles()
   
    """Retorna o número de linhas da matriz-mapa"""
    def get_line_len(self):
        return self._lines

    """Retorna o número de colunas da matriz-mapa"""
    def get_column_len(self):
        return self._columns

    """Retorna o Sprite de uma posição expecífica da matriz-mapa"""
    def get_tile(self, line, column):
        return self._map[line][column]

    """Muda o Sprite da matriz-mapa"""
    def set_tile(self, sprite, tileId, line, column):
        self._map[line][column] = sprite
        self._map_save[line][column] = tileId

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
    
    """Limpa todos os elementro da matriz"""
    def clear(self):
        for i in range(self._lines):
            for j in range(self._columns):
                self._map[i][j] = Sprite("null.png")
                self._map_save[i][j] = ''
        self.position_tiles()

    """Salva a matriz-mapa num arquivo com o nome especificado"""
    def save(self, name):
        file = open(name, 'w')
        for i in range(self._lines):
            for j in range(self._columns):
                curr = str(self._map_save[i][j])
                file.write(curr + '\n')