from .day1 import DayOne
from .day2 import DayTwo
from .day3 import DayThree
from .day4 import DayFour
from .day5 import DayFive
from .day6 import DaySix
from .day7 import DaySeven
from .day8 import DayEight

__app_name__ = "Advent of Code Command Line Interface for Answers"
__version__ = "0.1.0"
__app_description__ = "Advent of Code CLI tool to easily print answers to the console."
__epilog__ = "Keep it going!"


SUCCESS, ERR_DIR = range(2)

__all__ = [
    "DayOne",
    "DayTwo",
    "DayThree",
    "DayFour",
    "DayFive",
    "DaySix",
    "DaySeven",
    "DayEight",
]
