from game.models.door import Door
import constants as c
from game.controllers.point import Point
class Room:
    def __init__(self, x, y):
        self._column = x
        self._row = y
        self._visited = False
        self._neighbors = []
        self._previous_room = {}
        self._next_room = {}
        self._doors = []
        self._path_index = None

    def __getitem__(self, item):
        return getattr(self, item)

    def find_by_coords(self, x, y):
        """
        Returns a truthy statement if the coordinates provide match the coordinates of the room
        """
        return True if self._row == x and self._column == y else False

    def set_visited(self):
        self._visited = True

    def get_row(self):
        return self._row

    def get_column(self):
        return self._column

    def set_neighbors(self, maze):
        current= [self.get_column(), self.get_row()]
        self._neighbors = maze._path.find_neighbors(current)

    def get_neighbors(self):
        return self._neighbors

    def get_next_room(self):
        return self._next_room

    def get_path_index(self):
        return self._path_index

    def set_path_index(self, index):
        self._path_index = index

    def get_previous_room(self):
        return self._previous_room

    def set_next_room(self, room):
        self._next_room = room
    
    def set_previous_room(self, room):
        self._previous_room = room

    def get_doors(self):
        return self._doors
    
    def add_door(self, door):
        self._doors.append(door)

    def set_doors(self, maze):
        l = c.LOCATIONS
        for i, n in enumerate(self._neighbors):
            p = Point(l[i][0], l[i][1])
            if 0 <= n[0] < c.MAZE_WIDTH and 0 <= n[1] < c.MAZE_HEIGHT:
                room = maze.find_room(n[0], n[1])
                if self._path_index + 1 == room._path_index:
                    door = Door(1, 1)
                    door.set_character('#')
                    door.set_position(p)
                    print(door._position.get_x(), door._position.get_y())
                    door.set_color(c.WHITE)
                    door.set_font_size(15)
                    self.add_door(door)
                elif self._path_index - 1 == room._path_index:
                    door = Door(1, -1)
                    door.set_position(p)
                    print(door._position.get_x(), door._position.get_y())
                    door.set_color(c.WHITE)
                    door.set_font_size(15)
                    door.set_character('#')
                    self.add_door(door)
                else:
                    door = Door(0, 0)
                    door.set_position(p)
                    print(door._position.get_x(), door._position.get_y())
                    door.set_color(c.WHITE)
                    door.set_font_size(15)
                    door.set_character('#')
                    self.add_door(door)


                