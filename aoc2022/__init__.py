from .day1 import DayOne
from .day2 import DayTwo
from .day3 import DayThree
from .day4 import DayFour

__app_name__ = "Advent of Code Command Line Interface for Answers"
__version__ = "0.1.0"
__app_description__ = "Advent of Code CLI tool to easily print answers to the console."
__epilog__ = "Keep it going!"


SUCCESS, ERR_DIR = range(2)

__all__ = ["DayOne", "DayTwo", "DayThree", "DayFour"]
