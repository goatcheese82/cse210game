from calendar import c
import imp
import random
from game.models.room import Room
from game.services.procedure_generator import ProcedureGenerator

class Path:
    def __init__(self, height, width):
        self._height = height
        self._width = width
        self._used = []
        self._procedure = []
        self._start = [0, 0]
    def build_procedure(self, maze):
        current = self._start[0]
        next = self.find_possible(current)
        while next:
            next = self.find_possible(current)
            current = next
        
    def find_start(self):
        self._start[0] = random.randint(0, self._width - 1)
        self._start[1] = random.randint(0, self._height - 1)
        print(self._start)
    
    def find_possible(self, current):
        neighbors = [
            [current[0], current[1] + 1], 
            [current[0], current[1] -1], 
            [current[0] + 1, current[1]], 
            [current[0] -1, current[1]]
            ]
        possible = []
        for i in neighbors:
            if i[0] >= 0 and i[1] >= 0:
                print(i)
                possible.append(i)
        if len(possible) < 1:
            return False
        choice = random.choice(possible)
        while choice in self._used:
            choice = random.choice(possible)
        return choice