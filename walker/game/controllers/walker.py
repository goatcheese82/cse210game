import time
import pyray
from game.controllers.point import Point
import constants as c
from game.models.message import Message


class Walker:

    def __init__(self, video_service, keyboard_service, message):
        self._ks = keyboard_service
        self._vs = video_service
        self._message = message

    def start_game(self, player, maze):
      self._vs.open_window()
      while self._vs.is_window_open():
         t = pyray.get_time()
         self._message.update_message("")
         self._get_inputs(player, maze)
         self._do_updates(player, maze, t)
         self._do_outputs(player, maze)
      self._vs.close_window()

    def game_over(self, t):
        if t < 199:
           self._message.update_message('Great! You won!')
        else:
           self._message.update_message('You Lose!')
           return

    def _get_inputs(self, player, maze):
        player = player
        velocity = self._ks.get_direction()
        player.set_velocity(velocity)

    def _do_updates(self, player, maze, t):
         if t > 199 or maze.get_current_room() == maze.get_room_path()[-1]:
            self.game_over(t)
         player.move_next()
         for e in maze.get_current_room().get_doors():
            if player.get_position().equals(e.get_position()):
                if e.get_status() == 1:
                    maze.advance_room(e.get_direction())
                    position = Point(int(c.MAX_X / 2), int(c.MAX_Y / 2))
                    player.set_position(position)
                else:
                   self._message.update_message("This door is locked!")

    def _do_outputs(self, player, maze):
        self._vs.clear_buffer()
        self._vs.draw_actor(player)
        self._vs.draw_actor(self._message)
        self._vs.draw_actors(maze.get_current_room().get_doors())
        self._vs.flush_buffer()
