from collections import namedtuple

# Colors as a class with direct color values
class Color:
  WHITE = (255, 255, 255)
  BLACK = (0, 0, 0)

  DARK_GRAY = (80, 80, 80)
  GRAY = (150, 150, 150)
  LIGHT_GRAY = (220, 220, 220)
  RED = (255, 0, 0)
  GREEN = (0, 180, 0)
  BLUE = (0, 0, 255)
  YELLOW = (255, 255, 0)
  PURPLE = (128, 0, 128)
  ORANGE = (255, 165, 0)
  CYAN = (0, 255, 255)

XY = namedtuple("XY", ["x", "y"])