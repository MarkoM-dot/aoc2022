import argparse
from typing import Optional, Sequence

import aoc2022
from aoc2022 import SUCCESS, __app_description__, __app_name__, __epilog__, __version__

from .solution_template import solutionizer
from .translations import index_to_word


def view_solution(num_day: str):
    class_name = f"Day{num_day}"
    try:
        klass = getattr(aoc2022, class_name)
        part_one, part_two = solutionizer(klass())
        print("=*=" * 20)
        print(f"{class_name} Part 1", part_one)
        print(f"{class_name} Part 2", part_two)
        print("=*=" * 20)
    except AttributeError:
        pass


def action(day: int):
    if day:
        view_solution(index_to_word[day])
    else:
        [view_solution(day) for day in index_to_word]


def aoc_day(day: str) -> int:
    try:
        value = int(day)
    except ValueError:
        raise argparse.ArgumentTypeError(f"Expected integer got {day!r}")

    if value not in range(1, 26):
        raise argparse.ArgumentTypeError(
            f"Expected Advent of Code Day in range (1-25) got {day!r}"
        )

    return value


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        prog=__app_name__, description=__app_description__, epilog=__epilog__
    )

    parser.add_argument("--version", action="version", version=__version__)
    parser.add_argument(
        "-d",
        "--day",
        type=aoc_day,
        help="AOC puzzle day. Must be an integer between 1 and 25 inclusive.",
        required=False,
    )

    args = vars(parser.parse_args(argv))
    action(**args)

    return SUCCESS
