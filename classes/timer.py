from dataclasses import dataclass
import pygame
@dataclass
class Timer():
  clock: pygame.time.Clock
  time: float = 0.0
  single_second_timer: float = 0.0
  fps: int = 60.0
  
  def __init__(self, clock: pygame.time.Clock, fps: int = 60):
    self.clock = clock
    self.fps = fps
    self.frame_time = 1000 / self.fps


  def tick(self):
    dt = self.clock.tick(self.fps)
    self.time += dt
    self.single_second_timer += dt
    if self.single_second_timer >= self.frame_time:
      self.single_second_timer = 0.0
      return True
    return False

