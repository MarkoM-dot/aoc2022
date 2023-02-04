from __future__ import annotations
import math
from pathlib import Path

from .solution_template import SolutionClass


class Vector:
    def __init__(self, x: int = 0, y: int = 0) -> None:
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x!r}, {self.y!r})"

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(self.x or self.y)

    def __eq__(self, other: Vector):
        return tuple(self) == tuple(other)

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __add__(self, other: Vector):
        return Vector(self.x + other.x, self.y + other.y)

    def __radd__(self, other: Vector):
        return self + other

    def __mul__(self, scalar: int):
        return Vector(self.x * scalar, self.y * scalar)

    def is_touching(self, other: Vector):
        return abs(self.x - other.x) <= 1 and abs(self.y - other.y) <= 1

    def follow(self, other: Vector):
        sin_x = 0 if other.x == self.x else (other.x - self.x) / abs(other.x - self.x)
        sin_y = 0 if other.y == self.y else (other.y - self.y) / abs(other.y - self.y)

        self.x += int(sin_x)
        self.y += int(sin_y)
        return self

    @property
    def coordinates(self) -> tuple[int, int]:
        return self.x, self.y


class Rope:
    def __init__(self) -> None:
        self.head = Vector()
        self.tail = Vector()
        self.motions: dict[str, Vector] = {
            "R": Vector(1, 0),
            "L": Vector(-1, 0),
            "U": Vector(0, 1),
            "D": Vector(0, -1),
        }
        self.tail_visits: set[tuple[int, int]] = {(0, 0),}
        self.knots: list[Vector] = [Vector() for _ in range(10)]
        self.knot_tail_visits: set[tuple[int, int]] = set()

    def move(self, direction: str, steps: int):
        for _ in range(steps):
            self.head += self.motions[direction]
            if not self.tail.is_touching(self.head):
                self.tail.follow(self.head)
                self.tail_visits.add(self.tail.coordinates)

    def move_knots(self, direction: str, steps: int):
        for _ in range(steps):
            self.knots[0] += self.motions[direction]

            for i in range(1, 10):
                head = self.knots[i - 1]
                tail = self.knots[i]

                if not tail.is_touching(head):
                    tail.follow(head)
            self.knot_tail_visits.add(self.knots[-1].coordinates)


class DayNine(SolutionClass):
    def __init__(self) -> None:
        self.rope = Rope()

    @property
    def data_path(self) -> Path:
        return Path.cwd() / "data/year_2022_day_9.txt"

    def part_one(self, data: str) -> str:
        for motion in (line.split() for line in data.splitlines()):
            match motion:
                case [direction, steps]:
                    self.rope.move(direction, int(steps))
                case _:
                    raise SyntaxError(f"Unrecognized syntax: {motion}")
        return str(len(self.rope.tail_visits))

    def part_two(self, data: str) -> str:
         for motion in (line.split() for line in data.splitlines()):
            match motion:
                case [direction, steps]:
                    self.rope.move_knots(direction, int(steps))
                case _:
                    raise SyntaxError(f"Unrecognized syntax: {motion}")
         return str(len(self.rope.knot_tail_visits))

