import unittest
from collections import deque

from aoc2022.day6 import DaySix

part_one_data = (
    ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", "7"),
    ("bvwbjplbgvbhsrlpgdmjqwftvncz", "5"),
    ("nppdvjthqldpwncqszvftbrmjlhg", "6"),
    ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", "10"),
    ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", "11"),
)

deque_data = (
    (deque(["A", "B", "C"]), True),
    (deque(["A", "B", "A"]), False),
    (deque(["q", "B", "t"]), True),
)


class TestDaySix(unittest.TestCase):
    def setUp(self) -> None:
        self.solver = DaySix()

    def test_part_one(self):
        for input, expected in part_one_data:
            with self.subTest(
                "Testing first start-of-packet marker...",
                input=input,
                expected=expected,
            ):
                self.assertEqual(self.solver.part_one(input), expected)

    def test_is_unique_substring(self):
        for input, expected in deque_data:
            with self.subTest(
                "Testing unique sequence...", input=input, expected=expected
            ):
                self.assertEqual(self.solver.is_unique_substring(input), expected)
