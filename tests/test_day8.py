import unittest

from aoc2022.day8 import DayEight

part_one_data = (("30373\n25512\n65332\n33549\n35390\n", "21"),)

part_two_data = (("30373\n25512\n65332\n33549\n35390\n", "8"),)


class TestDayEight(unittest.TestCase):
    def setUp(self) -> None:
        self.solver = DayEight()

    def test_part_one(self):
        for input, expected in part_one_data:
            with self.subTest(
                "Testing first start-of-packet marker part one...",
                input=input,
                expected=expected,
            ):
                self.assertEqual(self.solver.part_one(input), expected)

    def test_two_one(self):
        for input, expected in part_two_data:
            with self.subTest(
                "Testing ...",
                input=input,
                expected=expected,
            ):
                self.assertEqual(self.solver.part_two(input), expected)
