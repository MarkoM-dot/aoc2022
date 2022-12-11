from pathlib import Path
from .solution_template import SolutionClass


Section = tuple[int, int]

class DayFour(SolutionClass):
    @property
    def data_path(self) -> Path:
        return Path.cwd() / "data/year_2022_day_4.txt"

    def fully_contains(self, first_section: Section, second_section: Section) -> bool:
        min_one, max_one = first_section
        min_two, max_two = second_section
        if min_one <= min_two and max_one >= max_two:
            return True
        if min_one >= min_two and max_one <= max_two:
            return True
        
        return False

    def part_one(self, data: str) -> int:
        sections = [[tuple(int(section) for section in assignment.split("-")) for assignment in line.split(",")] for line in data.splitlines()]
        return sum(self.fully_contains(*section) for section in sections)
    
    def part_two(self, data: str) -> int:
        ...
