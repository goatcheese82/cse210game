from game.models.room import Room
from game.models.path import Path

class Maze:
    def __init__(self, width, height):
        self._width = width
        self._height = height
        self._rooms = []
        self._path = {}
    def populate_grid(self):
        for r in range(self._height):
            for c in range(self._width):
                room = Room(r, c)
                self._rooms.append(room)
    def add_path(self):
        path = Path(self._height, self._width)
        self._path = path
    def get_width(self):
        return self._width
    def get_height(self):
        return self._height
    def find_room(self, x, y):
        return list(filter(lambda room: room['_row'] == y and room['_column'] == x, self._rooms))[0]
    
    def print_self(self):
        current = [0, 0]
        for r in range(self._height):
            current[0] = r
            print('|', end='')
            for c in range(self._width):
                current[1] = c
                print(current, end='')
            print('|')
