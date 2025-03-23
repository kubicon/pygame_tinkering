from classes.button import Button
from classes.general_classes import XY, Color
from classes.counter import Counter


class MainButton(Button):
  def __init__(self, b_pos: XY, b_size: XY, text: str, color: Color, hover_color: Color, counter: Counter):
    super().__init__(b_pos, b_size, text, color, hover_color)
    self.counter = counter

  def handle_click(self):
    self.counter.increase()