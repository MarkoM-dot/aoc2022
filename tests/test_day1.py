import unittest

from aoc2022.day1 import DayOne

data_part_one = [
    ("1000\n2000\n3000\n\n4000\n\n5000\n6000\n\n7000\n8000\n9000\n\n10000\n", 24000),
    ("10\n20\n\n15\n", 30),
    ("1000\n", 1000),
    ("2000\n\n5000\n\n1000\n1000\n4000\n\n5000\n", 6000),
]

data_part_two = [
    ("1000\n2000\n3000\n\n4000\n\n5000\n6000\n\n7000\n8000\n9000\n\n10000\n", 45000),
]


class TestDayOne(unittest.TestCase):
    def setUp(self) -> None:
        self.solver = DayOne()

    def test_part_one(self):
        for input, expected in data_part_one:
            with self.subTest(
                "Testing highest calories...", input=input, expected=expected
            ):
                self.assertEqual(self.solver.part_one(input), expected)

    def test_part_two(self):
        for input, expected in data_part_two:
            with self.subTest(
                "Testing sum of three highest calories...",
                input=input,
                expected=expected,
            ):
                self.assertEqual(self.solver.part_two(input), expected)
