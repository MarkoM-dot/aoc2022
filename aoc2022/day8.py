from pathlib import Path
from typing import Optional

from .solution_template import SolutionClass


class Tree:
    def __init__(
        self,
        z: int,
        above: Optional["Tree"] = None,
        below: Optional["Tree"] = None,
        left: Optional["Tree"] = None,
        right: Optional["Tree"] = None,
    ):
        self.z = z
        self.above = above
        self.below = below
        self.left = left
        self.right = right

    def __repr__(self):
        return f"Tree({self.z})"


class Terrain:
    def __init__(self, data: list[str]) -> None:
        self.rows = len(data[0])
        self.columns = len(data)
        self.terrain = {
            (x, y): Tree(int(z))
            for y, nums in enumerate(data)
            for x, z in enumerate(nums)
        }

        for y in range(self.columns):
            prev = None
            for x in range(self.rows):
                current = self.terrain[(x, y)]
                if prev:
                    prev.right = current
                current.left = prev
                prev = current

        for x in range(self.rows):
            prev = None
            for y in range(self.columns):
                current = self.terrain[(x, y)]
                if prev:
                    prev.above = current
                current.below = prev
                prev = current

    def scenic_score(self, tree: Tree) -> int:
        above, below, right, left = tree.above, tree.below, tree.right, tree.left
        trees_above = trees_below = trees_right = trees_left = 0

        while above:
            trees_above += 1
            if above.z >= tree.z:
                break
            above = above.above

        while below:
            trees_below += 1
            if below.z >= tree.z:
                break
            below = below.below

        while right:
            trees_right += 1
            if right.z >= tree.z:
                break
            right = right.right

        while left:
            trees_left += 1
            if left.z >= tree.z:
                break
            left = left.left

        return trees_above * trees_below * trees_right * trees_left

    def max_scenic_score(self) -> int:
        return max((self.scenic_score(tree) for tree in self.terrain.values()))


class DayEight(SolutionClass):
    @property
    def data_path(self) -> Path:
        return Path.cwd() / "data/year_2022_day_8.txt"

    def part_one(self, data: str) -> str:
        matrix = [[int(n) for n in nums] for nums in data.splitlines()]
        trees = set()

        # check rows from left to right
        for y, m in enumerate(matrix):
            peak = -1
            for x, z in enumerate(m):
                if z > peak:
                    trees.add((x, y, z))
                    peak = z

        # check rows from right to left
        for y, m in enumerate(matrix):
            peak = -1
            for x in range(len(m) - 1, 0, -1):
                z = m[x]
                if z > peak:
                    trees.add((x, y, z))
                    peak = z

        # check columns from top to bottom
        for x in range(1, len(matrix[0]) - 1):
            peak = -1
            for y, m in enumerate(matrix):
                z = m[x]
                if z > peak:
                    trees.add((x, y, z))
                    peak = z

        # check columns from bottom to top
        for x in range(1, len(matrix)):
            peak = -1
            for y in range(len(matrix[0]) - 1, 0, -1):
                z = matrix[y][x]
                if z > peak:
                    trees.add((x, y, z))
                    peak = z

        return str(len(trees))

    def part_two(self, data: str) -> str:
        terrain = Terrain(data.splitlines())
        return str(terrain.max_scenic_score())
