from abc import ABC, abstractmethod


class EventObject(ABC):
  @abstractmethod
  def handle_event(self, event, mouse_pos):
    assert False, "handle_event must be implemented in subclass"


    
class RenderObject(ABC):
  @abstractmethod
  def render(self, surface):
    assert False, "render must be implemented in subclass"