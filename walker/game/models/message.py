from game.models.element import Element

class Message(Element):
   def __init__(self):
      super().__init__()
   
   def update_message(self, message):
      self.set_character(message)