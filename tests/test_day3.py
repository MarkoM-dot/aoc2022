import unittest

from aoc2022.day3 import DayThree

part_one_data = (
    (
        "vJrwpWtwJgWrhcsFMMfFFhFp\njqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\nPmmdzqPrVvPwwTWBwg\nwMqvLMZHhHMvwLHjbvcjnnSBnvTQFn\nttgJtRGJQctTZtZT\nCrZsJsPPZsGzwwsLwLmpwMDw\n",
        157,
    ),
)

part_one_rucksacks = (
    ("vJrwpWtwJgWrhcsFMMfFFhFp", "vJrwpWtwJgWr", "hcsFMMfFFhFp"),
    ("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", "jqHRNqRjqzjGDLGL", "rsFMfFZSrLrFZsSL"),
    ("PmmdzqPrVvPwwTWBwg", "PmmdzqPrV", "vPwwTWBwg"),
)

part_one_item_priorities = (
    ("p", 16),
    ("L", 38),
    ("P", 42),
    ("v", 22),
    ("t", 20),
    ("s", 19),
)

part_one_common_item = (
    ("vJrwpWtwJgWr", "hcsFMMfFFhFp", "p"),
    ("jqHRNqRjqzjGDLGL", "rsFMfFZSrLrFZsSL", "L"),
    ("PmmdzqPrV", "vPwwTWBwg", "P"),
)


class TestDayThree(unittest.TestCase):
    def setUp(self) -> None:
        self.solver = DayThree()

    def test_part_one(self):
        for input, expected in part_one_data:
            with self.subTest(
                "Testing sum of priorities of item types...",
                input=input,
                expected=expected,
            ):
                self.assertEqual(self.solver.part_one(input), expected)

    def test_split_rucksack(self):
        for input, first_compartment, second_compartment in part_one_rucksacks:
            with self.subTest(
                "Test splitting rucksack into compartments...",
                input=input,
                first_compartment=first_compartment,
                second_compartment=second_compartment,
            ):
                self.assertEqual(
                    self.solver.split_rucksack(input),
                    (first_compartment, second_compartment),
                )

    def test_item_priority(self):
        for input, expected in part_one_item_priorities:
            with self.subTest("Test item priorities given types..."):
                self.assertEqual(self.solver.item_priority(input), expected)

    def test_find_common_item(self):
        for first_compartment, second_compartment, expected in part_one_common_item:
            with self.subTest(
                "Test find common item in compartments...",
                first_compartment=first_compartment,
                second_compartment=second_compartment,
                expected=expected,
            ):
                self.assertEqual(
                    self.solver.find_common_item(first_compartment, second_compartment),
                    expected,
                )
