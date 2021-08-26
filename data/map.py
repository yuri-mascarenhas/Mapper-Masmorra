from data.PPlay.gameimage import *
from math import ceil
from data.tile import *
from copy import copy

class Map(object):
    """
    Define o Mapa a ser construído/salvo
    """
    #--------------------Atributos--------------------
    _map: list[list[list[Tile]]] = []      # Matriz de Tiles com as posições já setadas
    _map_save: list[list[list[int]]] = []  # Matriz que guarda os códigos de cada tile em sua posição para ser salvo

    lines: int
    columns: int
    layers: int
    _grid = { "x": 0, "y": 0 }

    _background: GameImage
    _default_tile: str

    #--------------------Métodos--------------------
    def __init__(self, size_x: int, size_y: int, grid_x: int, grid_y: int, layers: int = 1, default_background: str = "resources/background/default.png", default_tile: str ="resources/null.png"):
        self.lines = ceil(size_x / grid_x)
        self.columns = ceil(size_y / grid_y)
        self.layers = layers

        self._grid["x"] = grid_x
        self._grid["y"] = grid_y

        self._background = GameImage(default_background)
        self._default_tile = default_tile

        for z in range(self.layers):
            self._map.append([])
            self._map_save.append([])
            for i in range(self.lines):
                self._map[z].append([])
                self._map_save[z].append([])
                for _ in range(self.columns):
                    self._map[z][i].append(Tile(self._default_tile, 1, z))
                    self._map_save[z][i].append(0)
    
    """Desenha a matriz-mapa"""
    def draw(self):
        self._background.draw()
        for z in range(self.layers):
            for x in range(self.lines):
                for y in range(self.columns):
                    if(self._map[z][x][y].total_frames > 1): self._map[z][x][y].update()
                    self._map[z][x][y].draw_at(x * self._grid["x"], y * self._grid["y"])

    """Retorna o Tile de uma posição expecífica da matriz-mapa"""
    def get_tile(self, layer: int, line: int, column: int):
        return self._map[layer][line][column]

    """Muda o Tile de uma posição expecífica da matriz-mapa"""
    def set_tile(self, tile: Tile, layer: int, line: int, column: int):
        self._map[layer][line][column] = copy(tile)
        self._map_save[layer][line][column] = tile.id
    
    """Apaga o Tile de uma posição expecífica da matriz-mapa"""
    def delete_tile(self, layer: int, line: int, column: int):
        self._map[layer][line][column] = Tile(self._default_tile, 1, layer)
        self._map_save[layer][line][column] = 0
    
    """Limpa todos os elementro da matriz-mapa"""
    def clear(self):
        for z in range(self.layers):
            for x in range(self.lines):
                for y in range(self.columns):
                    self.delete_tile(z, x, y)

    """Salva a matriz-mapa num arquivo com o nome especificado"""
    def save(self, name: str = "resources/maps/map1.txt"):
        file = open(name, 'w')
        for z in range(self.layers):
            for x in range(self.lines):
                for y in range(self.columns):
                    curr = str(self._map_save[z][x][y])
                    file.write(curr + " ")
                file.write("\n")
            if(z < self.layers - 1): file.write("-\n")
