class ProcedureGenerator:
    def __init__(self, maze):
        self._maze = maze
    def move_up(self, spot):
        if spot[0] > 0:
            spot[0] += -1
    def move_right(self, spot):
        if spot[1] < self._maze._width:
            spot[1] += 1
    def move_left(self, spot):
        if spot[1] > 0:
            spot[1] += -1
    def move_down(self, spot):
        if spot[0] < self._maze._height:
            spot[0] += -1
    