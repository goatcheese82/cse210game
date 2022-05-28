from game.models.question import Question

class Room:
    def __init__(self, x, y):
        self._question = Question()
        self._row = x
        self._column = y
        self._visited = False
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