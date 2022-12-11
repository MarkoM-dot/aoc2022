from pathlib import Path
from solution_template import SolutionClass


class DaySix(SolutionClass):
    @property
    def data_path(self) -> Path:
        return Path.cwd() / "data/year_2022_day_6.txt"

    def part_one(self, data: str) -> str:
        ...

    def part_two(self, data: str) -> str:
        ...
