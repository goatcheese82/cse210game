from game.models.element import Element
class Door(Element):

   def __init__(self, status, direction):
      super().__init__()
      self._status = status
      self._direction = direction

   def get_status(self):
      return self._status

   def set_status(self, status):
      self._status = status

   def get_direction(self):
      return self._direction

   def set_direction(self, direction):
      self._direction = direction