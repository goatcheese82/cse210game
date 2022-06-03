from game.models.element import Element

class Player(Element):

   def __init__(self):
      super().__init__()

   def get_score(self):
      return self._score

   def set_score(self, score):
      self._score = score