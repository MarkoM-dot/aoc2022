from pathlib import Path

from .solution_template import SolutionClass


class DayTwo(SolutionClass):
    def __init__(self) -> None:
        self.points = {"X": 1, "Y": 2, "Z": 3}
        self.rule_map = {"X": {"A": 3, "B": 0, "C": 6}, "Y": {"A": 6, "B": 3, "C": 0}, "Z": {"A": 0, "B": 6, "C": 3}}
        self.forcing_map = {"A": {"X": "Z", "Y": "X", "Z": "Y"}, "B": {"X": "X", "Y": "Y", "Z": "Z"}, "C": {"X": "Y", "Y": "Z", "Z": "X"}}
        
    @property
    def data_path(self):
        return Path.cwd() / "data/year_2022_day_2.txt"

    def get_plays(self, data: str) -> list[str]:
        strategies = data.split("\n")
        strategies.pop()
        return strategies

    def play_outcome(self, play: str) -> int:
        point = self.points[play[2]]
        result = self.rule_map[play[2]][play[0]]
        return point + result

    def force_move(self, play: str) -> str:
        find_move = self.forcing_map[play[0]][play[2]]
        return play[:-1] + find_move

    def part_one(self, data: str) -> int:
        plays = self.get_plays(data)
        return sum([self.play_outcome(play) for play in plays])

    def part_two(self, data: str) -> int:
        plays = self.get_plays(data)
        return sum([self.play_outcome(self.force_move(play)) for play in plays])


