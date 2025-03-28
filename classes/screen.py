
import pygame
 
class Screen:
  def __init__(self, screen: pygame.Surface, default_color: Color):
    self.screen = screen
    self.default_color = default_color

  def draw_screen(self):
    self.screen.fill(self.default_color)

  def draw_object(self, object: RenderObject):
    self.screen.blit(object.image, object.rect)
