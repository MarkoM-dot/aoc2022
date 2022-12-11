import unittest

from aoc2022.day4 import DayFour

part_one_data = (("2-4,6-8\n2-3,4-5\n5-7,7-9\n2-8,3-7\n6-6,4-6\n2-6,4-8", 2),)

containment_data = (
    (((2, 4), (6, 8)), False),
    (((2, 3), (4, 5)), False),
    (((5, 7), (7, 9)), False),
    (((2, 8), (3, 7)), True),
    (((6, 6), (4, 6)), True),
    (((2, 6), (4, 8)), False),
)


class TestDayFour(unittest.TestCase):
    def setUp(self) -> None:
        self.solver = DayFour()

    def test_part_one(self):
        for input, expected in part_one_data:
            with self.subTest(
                "Testing assignment pairs containment...",
                input=input,
                expected=expected,
            ):
                self.assertEqual(self.solver.part_one(input), expected)

    def test_fully_contains(self):
        for input, expected in containment_data:
            with self.subTest(
                "Testing fully contains method...", input=input, expected=expected
            ):
                self.assertEqual(self.solver.fully_contains(*input), expected)
