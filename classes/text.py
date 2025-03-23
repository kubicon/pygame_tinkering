import pygame

from classes.abstract_classes import RenderObject


class Text(RenderObject):
  def __init__(self, pos, text, font_size, color):
    self.pos = pos
    self.text = text
    self.font = pygame.font.Font(None, font_size)
    self.color = color

  def render(self, surface):
    text_surface = self.font.render(self.text, True, self.color)
    # text_rect = text_surface.get_rect(center=self.pos)
    surface.blit(text_surface, self.pos)
   