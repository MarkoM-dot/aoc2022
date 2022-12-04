from pathlib import Path

from .solution_template import SolutionClass


class DayOne(SolutionClass):
    @property
    def data_path(self):
        return Path.cwd() / "data/year_2022_day_1.txt"

    def elf_loads(self, data: str) -> list[int]:
        elves_loads = [x.split("\n") for x in data.split("\n\n")]
        return [
            sum(int(x) for x in elf_load if x.isdigit()) for elf_load in elves_loads
        ]

    def part_one(self, data: str) -> int:
        """
        Highest calories given a list of snacks and their calories per elf.
        """
        return max(self.elf_loads(data))

    def part_two(self, data: str) -> int:
        """
        Sum of three highest calories given a list of calories carried by each elf.
        """
        return sum(sorted(self.elf_loads(data), reverse=True)[:3])
