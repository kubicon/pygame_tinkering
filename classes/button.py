
import pygame

from classes.general_classes import XY, Color
from classes.abstract_classes import EventObject, RenderObject

class Button(EventObject, RenderObject):
  def __init__(self, b_pos: XY, b_size: XY, text: str, color: Color, hover_color: Color):
    self.rect = pygame.Rect(*b_pos, *b_size)
    self.text = text
    self.color = color
    self.hover_color = hover_color
    self.current_color = self.color
    self.font = pygame.font.Font(None, 32)
    self.is_clicked = False 
  
  
  def render(self, surface):
    # Draw button
    pygame.draw.rect(surface, self.current_color, self.rect, border_radius=8)
    pygame.draw.rect(surface, Color.BLACK, self.rect, 2, border_radius=8)  # Border
    
    # Draw text
    text_surface = self.font.render(self.text, True, Color.BLACK)
    text_rect = text_surface.get_rect(center=self.rect.center)
    surface.blit(text_surface, text_rect)
  
  def handle_event(self, event, mouse_pos):
    # Check button hover
    self.check_hover(mouse_pos)
      
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left click
      if self.check_click(mouse_pos, True):
        self.handle_click()

    if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
      self.reset_click_state()
    pass

  def check_hover(self, pos):
    if self.rect.collidepoint(pos):
      self.current_color = self.hover_color
      return True
    else:
      self.current_color = self.color
      return False
  
  def check_click(self, pos, click):
    if self.rect.collidepoint(pos) and click and not self.is_clicked:
      self.is_clicked = True 
      return True
    return False
  
  def reset_click_state(self):
    self.is_clicked = False

  def handle_click(self):
    assert False, "handle_click must be implemented in subclass"
 