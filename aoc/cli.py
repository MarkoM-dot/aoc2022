import argparse
from typing import Optional, Sequence

from aoc import SUCCESS, __app_description__, __app_name__, __epilog__, __version__

from .actions import Action


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
        "day",
        type=aoc_day,
        help="AOC puzzle day. Must be an integer between 1 and 25 inclusive.",
    )

    subparsers = parser.add_subparsers(dest="command")
    subparsers.required = True

    subparsers.add_parser("question", help="Get your puzzle question.")
    subparsers.add_parser("data", help="Get your puzzle input.")
    submit_parser = subparsers.add_parser(
        "submit",
        help="Submit your answer to the puzzle. You may specify which part with --part, 1 or 2. Defaults to part 1.",
    )

    submit_parser.add_argument(
        "-p",
        "--part",
        type=int,
        choices=range(1, 3),
        default=1,
        help="Which part during the day? 1 or 2. Default is 1.",
    )
    submit_parser.add_argument(
        "answer", type=int, help="Provide an answer to submit (required)."
    )

    args = vars(parser.parse_args(argv))
    action = Action(**args)
    action.do()

    return SUCCESS
