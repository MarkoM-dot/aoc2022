from pathlib import Path
from .solution_template import SolutionClass


class DayThree(SolutionClass):
    @property
    def data_path(self) -> Path:
        return Path.cwd() / "data/year_2022_day_3.txt"

    def item_priority(self, letter: str) -> int:
        if letter.islower():
            return ord(letter) - 96
        return ord(letter) - 38

    def split_rucksack(self, rucksack: str) -> tuple[str, str]:
        first_compartment, second_compartment = (
            rucksack[: len(rucksack) // 2],
            rucksack[len(rucksack) // 2 :],
        )
        return first_compartment, second_compartment

    def part_one(self, data: str) -> int:
        ...

    def part_two(self, data: str) -> int:
        ...
