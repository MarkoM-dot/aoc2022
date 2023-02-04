from pathlib import Path

from .solution_template import SolutionClass


class CentralProcessingUnit:
    def __init__(self):
        self.register = 1
        self.cycle = 0
        self.signal_strenghts: list[int] = []

    @property
    def cycle_check(self):
        return self.cycle == 20 or (self.cycle - 20) % 40 == 0

    def update_cycle(self):
        self.cycle += 1
        if self.cycle_check:
            self.signal_strenghts.append(self.cycle * self.register)

    def noop(self):
        self.update_cycle()

    def addx(self, value: int):
        self.update_cycle()
        self.update_cycle()
        self.register += value

    @property
    def signal_strength(self) -> int:
        return sum(self.signal_strenghts)




class DayTen(SolutionClass):
    def __init__(self) -> None:
        self.cpu = CentralProcessingUnit()

    @property
    def data_path(self) -> Path:
        return Path.cwd() / "data/year_2022_day_10.txt"

    def part_one(self, data: str) -> str:
        for instruction in (line.split() for line in data.splitlines()):
            match instruction:
                case ["noop"]:
                    self.cpu.noop()
                case ["addx", value]:
                    self.cpu.addx(int(value))
        return str(self.cpu.signal_strength)

    def part_two(self, data: str) -> str:
        return super().part_two(data)
