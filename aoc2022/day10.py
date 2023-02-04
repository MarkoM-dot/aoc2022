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


class CathodeRayTube:
    def __init__(self) -> None:
        self.register = 1
        self.screen: list[list[str]] = [["." for _ in range(40)] for _ in range(6)]
        self.cycle = 0

    def noop(self):
        screen_y = self.cycle // 40
        screen_x = self.cycle % 40

        if abs(screen_x - self.register) <= 1:
            self.screen[screen_y][screen_x] = "#"
        self.cycle += 1

    def addx(self, value: int):
        self.noop()
        self.noop()
        self.register += value

    @property
    def print_image(self):
        for i in self.screen:
            line = "".join(i)
            print(line)

    @property
    def image_as_str(self) -> str:
        text = []
        for line in self.screen:
            line.append("\n")
            text.append("".join(line))
        return "".join(text)


class DayTen(SolutionClass):
    def __init__(self) -> None:
        self.cpu = CentralProcessingUnit()
        self.crt = CathodeRayTube()

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
        for instruction in (line.split() for line in data.splitlines()):
            match instruction:
                case ["noop"]:
                    self.crt.noop()
                case ["addx", value]:
                    self.crt.addx(int(value))
        return self.crt.image_as_str
