from game.services.procedure_generator import ProcedureGenerator
from game.models.maze import Maze
from game.services.video_service import VideoService
import constants as c
from game.controllers.walker import Walker
from game.models.player import Player
from game.services.key_service import KeyService
from game.controllers.point import Point
from game.models.message import Message

def main():
    #Create the Maze
    maze = Maze(6, 6)
    maze.populate_grid()
    maze.add_path()
    maze._path.find_start()
    maze._path.build_path()
    maze.set_room_path()
    maze.update_doors()
    # print(maze._path._start)
    # maze.print_self()
    # maze._path.print_path()
    room = maze._room_path[0]
    room.set_neighbors(maze)
    maze.set_current_room(room)

    #Create the player
    x = int(c.MAX_X / 2)
    y = int(c.MAX_Y /2)
    position = Point(x, y)

    player = Player()
    player.set_character("**")
    player.set_font_size(c.FONT_SIZE)
    player.set_color(c.RED)
    player.set_position(position)

    ks = KeyService(c.CELL_SIZE)
    vs = VideoService(c.CAPTION, c.MAX_X, c.MAX_Y, c.CELL_SIZE, c.FRAME_RATE, False)
    message = Message()
    controller = Walker(vs, ks, message)
    controller.start_game(player, maze)


if __name__ == "__main__":
    main()