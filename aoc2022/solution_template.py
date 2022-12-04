from abc import ABC, abstractmethod, abstractproperty
from pathlib import Path


class SolutionClass(ABC):
    @abstractproperty
    def data_path(self) -> Path:
        ...

    @abstractmethod
    def part_one(self, data: str) -> int:
        ...

    @abstractmethod
    def part_two(self, data: str) -> int:
        ...


def solutionizer(solver: SolutionClass) -> tuple[int, int]:
    """
    Returns the answers for part one and part two given solution class.
    """
    path = solver.data_path

    with open(path, "r") as f:
        data = f.read()

    return solver.part_one(data), solver.part_two(data)
