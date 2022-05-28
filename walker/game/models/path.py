import random
from game.models.room import Room

class Path:
    def __init__(self, height, width):
        self._height = height
        self._width = width
        self._procedure = []
        self._start = [0, 0]
    def build_procedure(self, maze):
        current = self._start
        room = maze.find_room(current[0], current[1])       
    def find_start(self):
        self._start[0] = random.randint(0, self._width)
        self._start[1] = random.randint(0, self._height)