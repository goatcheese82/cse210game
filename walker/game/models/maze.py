from game.models.room import Room
from game.models.path import Path

class Maze:
    def __init__(self, width, height):
        self._width = width
        self._height = height
        self._current_room = {}
        self._rooms = []
        self._room_path = []
        self._path = {}

    def populate_grid(self):
        for r in range(self._height):
            for c in range(self._width):
                room = Room(c, r)
                self._rooms.append(room)
                
    def add_path(self):
        path = Path(self._height, self._width)
        self._path = path

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height

    def find_room(self, x, y):
        return list(filter(lambda room: room['_column'] == x and room['_row'] == y, self._rooms))[0]

    def advance_room(self, direction):
        next_room = self._room_path[self.get_current_room().get_path_index() + direction]
        self.set_current_room(next_room)
    
    def print_self(self):
        current = [0, 0]
        for r in range(self._height):
            current[1] = r
            print('|', end='')
            for c in range(self._width):
                current[0] = c
                print(current, end='')
            print('|')

    def get_current_room(self):
        return self._current_room
    
    def set_current_room(self, room):
        self._current_room = room
    
    def get_room_path(self):
        return self._room_path

    def update_doors(self):
        for i in self._room_path:
            i.set_doors(self)
    
    def get_path(self):
        return self._path


    def set_room_path(self):
        for i, r in enumerate(self._path._procedure):
            if r:
                room = self.find_room(r[0], r[1])
                room.set_neighbors(self)
                room.set_path_index(i)
            if len(self._room_path) > 0:
                previous_room = self._room_path[-1]
                previous_room.set_next_room(room)
                room.set_previous_room(previous_room)
            self._room_path.append(room)