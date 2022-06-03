from tkinter.tix import ROW
from game.models.color import Color


COLUMNS = 40
ROWS = 20
CELL_SIZE = 15
MAX_X = 900
MAX_Y = 600
FRAME_RATE = 15
FONT_SIZE = 15
CAPTION = "Escape"
SNAKE_LENGTH = 8
WHITE = Color(255, 255, 255)
RED = Color(255, 0, 0)
YELLOW = Color(255, 255, 0)
GREEN = Color(0, 255, 0)
MAZE_WIDTH = 6
MAZE_HEIGHT = 6
LOCATIONS = [[MAX_X - CELL_SIZE, int(MAX_Y / 2)], [0, int(MAX_Y / 2)], [int(MAX_X / 2), MAX_Y - CELL_SIZE], [int(MAX_X / 2), 0]]