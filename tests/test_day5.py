import unittest

from aoc2022.day5 import DayFive, StackCollection

part_one_data = (
    (
        "    [D]    \n[N] [C]    \n[Z] [M] [P]\n 1   2   3 \n\nmove 1 from 2 to 1\nmove 3 from 1 to 3\nmove 2 from 2 to 1\nmove 1 from 1 to 2\n",
        "CMZ",
    ),
)
drawing_to_stack_quantity = (
    (
        " 1   2   3 ",
        3,
    ),
)
part_two_data = (
    (
        "    [D]    \n[N] [C]    \n[Z] [M] [P]\n 1   2   3 \n\nmove 1 from 2 to 1\nmove 3 from 1 to 3\nmove 2 from 2 to 1\nmove 1 from 1 to 2\n",
        "MCD",
    ),
)


class TestDayFive(unittest.TestCase):
    def setUp(self) -> None:
        self.solver = DayFive()

    def test_part_one(self):
        for input, expected in part_one_data:
            with self.subTest(
                "Testing peeking each stack rearranged by CrateMover 9000...",
                input=input,
                expected=expected,
            ):
                self.assertEqual(self.solver.part_one(input), expected)

    def test_part_two(self):
        for input, expected in part_two_data:
            with self.subTest(
                "Testing peeking each stack rearranged by CrateMover9001...",
                input=input,
                expected=expected,
            ):
                self.assertEqual(self.solver.part_two(input), expected)

    def test_get_stack_quantity(self):
        for input, expected in drawing_to_stack_quantity:
            self.assertEqual(self.solver.get_stack_quantity(input), expected)


class TestStackCollection(unittest.TestCase):
    def setUp(self) -> None:
        self.stacks = StackCollection(3)
