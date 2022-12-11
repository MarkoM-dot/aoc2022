from collections import deque
from pathlib import Path
from typing import Deque

from .solution_template import SolutionClass


class DaySix(SolutionClass):
    @property
    def data_path(self) -> Path:
        return Path.cwd() / "data/year_2022_day_6.txt"

    def is_unique_substring(self, line: Deque[str]) -> bool:
        return len(line) == len(set(line))

    def find_start_of_packet_marker(self, line: str, sub_size: int = 4) -> int | None:
        substring = deque(line[:sub_size])
        marker = sub_size
        while marker < len(line):
            if self.is_unique_substring(substring):
                return marker
            substring.popleft()
            substring.append(line[marker])
            marker += 1
        return None

    def part_one(self, data: str) -> str:
        return str(self.find_start_of_packet_marker(data))

    def part_two(self, data: str) -> str:
        ...
