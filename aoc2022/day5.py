from pathlib import Path
from collections import deque
from typing import Deque
from .solution_template import SolutionClass


class StackCollection:
    def __init__(self, amount: int):
        self.stacks = [deque() for _ in range(amount)]

    def __len__(self):
        return len(self.stacks)

    def __iter__(self):
        for stack in self.stacks:
            yield stack

    def __getitem__(self, index):
        return self.stacks[index]

    def insert(self, line: tuple[str, ...]):
        for index, letter in enumerate(line):
            if not letter.isspace():
                self[index].appendleft(letter)

    def move(self, amount: int, origin: int, target: int):
        for _ in range(amount):
            self[target].append(self[origin].pop())

    @property
    def mass_peek(self) -> list[str]:
        return [stack[-1] for stack in self]


class DayFive(SolutionClass):
    @property
    def data_path(self) -> Path:
        return Path.cwd() / "data/year_2022_day_5.txt"

    def get_stack_quantity(self, line: str) -> int:
        return int(line.rstrip()[-1])

    def get_chars_from_line(self, line: str):
        return tuple(line[index] for index in range(1, len(line), 4))

    def parse_instruction(self, line: list[str]) -> tuple[int, int, int]:
        move, origin, target = int(line[1]), int(line[3]) - 1, int(line[5]) - 1
        return move, origin, target


    def init_configuration(self, drawing: list[str]):
        stack_amount = self.get_stack_quantity(drawing.pop())
        stacks = StackCollection(stack_amount)
        letters_by_line = tuple(self.get_chars_from_line(line) for line in drawing)

        for line in letters_by_line:
            stacks.insert(line)

        return stacks


    def part_one(self, data: str) -> str:
        drawing, instruction_set = data.split("\n\n")
        stacks = self.init_configuration(drawing.splitlines())

        for instruction in instruction_set.splitlines():
            movement = self.parse_instruction(instruction.split())
            stacks.move(*movement)

        return "".join(stacks.mass_peek)

    def part_two(self, data: str) -> int:
        return super().part_two(data)
