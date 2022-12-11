import unittest

from aoc2022 import DayFive

part_one_data = (
    (
        "    [D]    \n[N] [C]    \n[Z] [M] [P]\n 1   2   3 \n\nmove 1 from 2 to 1\nmove 3 from 1 to 3\nmove 2 from 2 to 1\nmove 1 from 1 to 2\n",
        "CMZ",
    ),
)


class DayFive(unittest.TestCase):
    def setUp(self) -> None:
        self.solver = DayFive()

    def test_part_one(self):
        for input, expected in part_one_data:
            with self.subTest(
                "Testing peeking each stack...", input=input, expected=expected
            ):
                self.assertEqual(self.solver.part_one(input), expected)
