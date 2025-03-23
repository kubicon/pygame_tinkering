import pygame

from classes.abstract_classes import RenderObject
from classes.counter import Counter
from classes.general_classes import XY, Color

class MainText(RenderObject):
  def __init__(self, pos: XY, font_size: int, color: Color, counter: Counter):
    self.pos = pos
    self.counter = counter
    self.font = pygame.font.Font(None, font_size)
    self.color = color

  def render(self, surface):
    text_surface = self.font.render(self.counter.get_count_str(), True, self.color)
    # text_rect = text_surface.get_rect(center=self.pos)
    surface.blit(text_surface, self.pos)
   