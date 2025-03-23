from dataclasses import dataclass
from classes.abstract_classes import EventObject


@dataclass
class Counter(EventObject):
  count: float = 0.0
  usual_multiplier: float = 1.0
  count_per_second: float = 0.1

  def increase(self, amount: float = 1.):
    self.count += amount

  def decrease(self, amount: float = 1.):
    self.count -= amount

  def get_count(self):
    return self.count
  
  def get_count_str(self):
    return str(self.count)
  
  def handle_event(self):
    self.increase(self.count_per_second * self.usual_multiplier)