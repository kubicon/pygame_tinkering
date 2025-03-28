import pygame

from classes.general_classes import XY, Color
from classes.main_button import MainButton
from classes.upgrade_button import UpgradeButton
from classes.main_text import MainText
from classes.counter import Counter
from classes.text import Text
from classes.timer import Timer
from classes.button import Button


class Game:
  def __init__(self):
    pygame.init()

    self.counter = Counter()
    self.timer = Timer(pygame.time.Clock())
    self.game_size = XY(1280, 720)
    button_size = XY(200, 60)
    button_pos = XY(self.game_size.x//2 - button_size.x//2, self.game_size.y//2 - button_size.y//2)
    upgrade_button_pos = XY(self.game_size.x//2 - button_size.x//2, self.game_size.y//2 + 80)

    main_text_pos = XY(self.game_size.x//2 - 80, self.game_size.y//2 - 80) 
    main_text = MainText(main_text_pos, 48, Color.GREEN, self.counter)
    main_button = MainButton(button_pos, button_size, "Click Me!", Color.GRAY, Color.GREEN, self.counter)
    upgrade_button = UpgradeButton(upgrade_button_pos, button_size, "Upgrade", 10, self.counter)
    
    self.render_objects = [main_button, upgrade_button, main_text]
    self.event_objects = [main_button, upgrade_button] 
    self.continuous_events = [self.counter]
    self.button_count = 0

  def draw_screen(self):
    '''Draw the screen, the order is important!'''
    self.screen.fill(Color.PURPLE)

    for render_object in self.render_objects:
      render_object.render(self.screen)
  
  def every_second_event(self):
    for event_object in self.continuous_events:
      event_object.handle_event() 

  def handle_frame(self):

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.running = False
        return
      
      # Get mouse position
      mouse_pos = pygame.mouse.get_pos()
      for event_object in self.event_objects:
        event_object.handle_event(event, mouse_pos)

    self.draw_screen()

  def run_game(self):
    self.running = True
    self.screen = pygame.display.set_mode(self.game_size) 

    while self.running:
      if self.timer.tick():
        self.every_second_event()
      self.handle_frame()
      pygame.display.flip() 

    pygame.quit()
 
def main():
  game = Game()
  game.run_game()


if __name__ == '__main__':
  main()