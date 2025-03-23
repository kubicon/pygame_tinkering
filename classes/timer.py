from dataclasses import dataclass

@dataclass
class Timer():
  time: float = 0.0
  single_second_timer: float = 0.0
  incremented_second: bool = False