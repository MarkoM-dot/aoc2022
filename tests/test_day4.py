import unittest

from aoc2022.day4 import DayFour


part_one_data = (
    ("2-4,6-8\n2-3,4-5\n5-7,7-9\n2-8,3-7\n6-6,4-6\n2-6,4-8", 2),
)
class TestDayFour(unittest.TestCase):
    def setUp(self) -> None:
        self.solver = DayFour()

    def test_part_one(self):
        for input, expected in part_one_data:
            with self.subTest("Testing assignment pairs containment...", input=input, expected=expected):
                self.assertEqual(self.solver.part_one(input), expected)

