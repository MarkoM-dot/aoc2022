from collections import deque
from pathlib import Path
from typing import NamedTuple, Optional

from .solution_template import SolutionClass


class File(NamedTuple):
    size: int
    name: str


class Directory:
    def __init__(self, name: str, parent: Optional["Directory"] = None):
        self.name: str = name
        self.parent = parent
        self.directories: list[Directory] = []
        self.files: list[File] = []

    def __repr__(self):
        return self.name

    def add_dir(self, directory: "Directory"):
        directory.parent = self
        self.directories.append(directory)

    def add_file(self, file: File):
        self.files.append(file)

    @property
    def size(self) -> int:
        size: int = 0
        if self.files:
            size += sum((file.size for file in self.files))
        if self.directories:
            size += sum((directory.size for directory in self.directories))
        return size


class FileSystem:
    """
    This file system assumes root is '/' and root has no parent.
    """

    def __init__(self):
        self.root = Directory("/")
        self.current = self.root

    @property
    def pwd(self) -> str:
        parent = self.current.parent
        if not parent:
            return self.current.name

        dirs = [self.current.name]
        while parent:
            dirs.append(parent.name)
            parent = parent.parent

        return "/".join(dirs[::-1])[1:]

    def cd(self, dir: str) -> Directory:
        if dir == "/":
            self.current = self.root
            return self.current

        if dir == "..":
            parent = self.current.parent
            if parent:
                self.current = parent
                return parent
            raise FileNotFoundError

        for d in self.current.directories:
            if d.name == dir:
                self.current = d
                return d
        raise FileNotFoundError

    @property
    def ls(self):
        return self.current.directories + self.current.files

    def du(self) -> list[tuple[str, int]]:
        """
        Return a list of all the directories providing their name and size as a tuple.
        """
        du = []
        qu = deque([self.root])

        while len(qu) > 0:
            d = qu.popleft()
            du.append((d.name, d.size))
            qu.extend(d.directories)
        return du


class TotalCommander:
    def __init__(self, data: str) -> None:
        self.data = data.splitlines()
        self.file_system = FileSystem()

    def scan_line(self, line: list[str]):
        match line:
            case ["$", "ls"]:
                pass
            case ["$", "cd", dir]:
                self.file_system.cd(dir)
            case ["dir", dir]:
                self.file_system.current.add_dir(Directory(dir))
            case [size, name] if size.isdigit():
                self.file_system.current.add_file(File(int(size), name))
            case _:
                raise ValueError(f"Unknown line to parse. Is this your line: {line}?")

    def work(self):
        for line in self.data:
            self.scan_line(line.split())


class DaySeven(SolutionClass):
    @property
    def data_path(self) -> Path:
        return Path.cwd() / "data/year_2022_day_7.txt"

    def part_one(self, data: str) -> str:
        tc = TotalCommander(data)
        tc.work()
        return str(sum((size for _, size in tc.file_system.du() if size <= 100_000)))

    def part_two(self, data: str) -> str:
        tc = TotalCommander(data)
        tc.work()

        free_space = 30_000_000 - (70_000_000 - tc.file_system.root.size)
        return str(min([size for _, size in tc.file_system.du() if size >= free_space]))
