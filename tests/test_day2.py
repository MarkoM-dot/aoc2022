import unittest

from aoc2022 import DayTwo

data_part_one = [
    ("A Y\nB X\nC Z\n", 15),
]

data_part_two = [
    ("A Y\nB X\nC Z\n", 12),
]


class TestDayTwo(unittest.TestCase):
    def setUp(self) -> None:
        self.solver = DayTwo()

    def test_strategy(self):
        for input, expected in data_part_one:
            with self.subTest(
                "Testing Rock, Paper, Scissors strategies...",
                input=input,
                expected=expected,
            ):
                self.assertEqual(self.solver.part_one(input), expected)

    def test_forcing_stratedy(self):
        for input, expected in data_part_two:
            with self.subTest(
                "Testing forcing moves...", input=input, expected=expected
            ):
                self.assertEqual(self.solver.part_two(input), expected)
