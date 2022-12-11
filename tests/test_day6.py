import unittest

from aoc2022.day6 import DaySix


part_one_data = (
    ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", "7"),
    ("bvwbjplbgvbhsrlpgdmjqwftvncz", "5"),
    ("nppdvjthqldpwncqszvftbrmjlhg", "6"),
    ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", "10"),
    ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", "11"),
)

class TestDaySix(unittest.TestCase):
    def setUp(self) -> None:
        self.solver = DaySix

    def test_part_one(self):
        for input, expected in part_one_data:
            with self.subTest(
                "Testing peeking each stack rearranged by CrateMover 9000...",
                input=input,
                expected=expected,
            ):
                self.assertEqual(self.solver.part_one(input), expected)


