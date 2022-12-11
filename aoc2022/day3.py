from pathlib import Path

from .solution_template import SolutionClass


class DayThree(SolutionClass):
    @property
    def data_path(self) -> Path:
        return Path.cwd() / "data/year_2022_day_3.txt"

    def item_priority(self, letter: str) -> int:
        """
        Return the item priority as an integer.

        ord() will return the integer representation of a unicode character:
        - ord("a") == 97
        - ord("A") == 65
        """
        if letter.islower():
            return ord(letter) - 96
        return ord(letter) - 38

    def split_rucksack(self, rucksack: str) -> tuple[str, str]:
        first_compartment, second_compartment = (
            rucksack[: len(rucksack) // 2],
            rucksack[len(rucksack) // 2 :],
        )
        return first_compartment, second_compartment

    def find_common_items(
        self, first_compartment: str, second_compartment: str
    ) -> set[str]:
        return {letter for letter in first_compartment if letter in second_compartment}

    def part_one(self, data: str) -> int:
        compartments = tuple(
            self.split_rucksack(rucksack) for rucksack in data.splitlines()
        )
        return sum(
            self.item_priority(*self.find_common_items(*compartment))
            for compartment in compartments
        )

    def unique_item(self, first, second, third) -> set[str]:
        return self.find_common_items(first, second).intersection(
            self.find_common_items(second, third)
        )

    def part_two(self, data: str) -> int:
        sack = iter(data.splitlines())
        uniques = [self.unique_item(*triplets) for triplets in zip(sack, sack, sack)]
        return sum(self.item_priority(*unique) for unique in uniques)
