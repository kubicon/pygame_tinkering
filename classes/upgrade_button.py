from classes.button import Button
from classes.general_classes import XY, Color
from classes.counter import Counter


class UpgradeButton(Button):
  def __init__(self, b_pos: XY, b_size: XY, text: str, cost: int, counter: Counter):

    self.cost = cost
    self.counter = counter
    self.color, self.hover_color = self.get_colors() 
    self.upgrade_name = text
    super().__init__(b_pos, b_size, text, self.color, self.hover_color)
    self.text = f"{self.upgrade_name} ({self.cost})"

  def get_colors(self):
    if self.counter.get_count() >= self.cost:
      return Color.WHITE, Color.LIGHT_GRAY
    else:
      return Color.GRAY, Color.DARK_GRAY
  
  def handle_click(self):
    if self.counter.get_count() >= self.cost:
      self.counter.decrease(self.cost)
      self.cost += 10
      self.text = f"{self.upgrade_name} ({self.cost})"
    
    
  def render(self, surface):
    self.color, self.hover_color = self.get_colors()
    super().render(surface) # Draw button