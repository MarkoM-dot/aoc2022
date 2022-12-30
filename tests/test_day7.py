import unittest

from aoc2022.day7 import DaySeven, Directory, File, FileSystem

part_one_data = (
    (
        "$ cd /\n$ ls\ndir a\n14848514 b.txt\n8504156 c.dat\ndir d\n$ cd a\n$ ls\ndir e\n29116 f\n2557 g\n62596 h.lst\n$ cd e\n$ ls\n584 i\n$ cd ..\n$ cd ..\n$ cd d\n$ ls\n4060174 j\n8033020 d.log\n5626152 d.ext\n7214296 k\n",
        "95437",
    ),
)
part_two_data = (
    (
        "$ cd /\n$ ls\ndir a\n14848514 b.txt\n8504156 c.dat\ndir d\n$ cd a\n$ ls\ndir e\n29116 f\n2557 g\n62596 h.lst\n$ cd e\n$ ls\n584 i\n$ cd ..\n$ cd ..\n$ cd d\n$ ls\n4060174 j\n8033020 d.log\n5626152 d.ext\n7214296 k\n",
        "24933642",
    ),
)


class TestDaySeven(unittest.TestCase):
    def setUp(self) -> None:
        self.solver = DaySeven()

    def test_part_one(self):
        for input, expected in part_one_data:
            with self.subTest(
                "Testing first start-of-packet marker part one...",
                input=input,
                expected=expected,
            ):
                self.assertEqual(self.solver.part_one(input), expected)

    def test_two_one(self):
        for input, expected in part_two_data:
            with self.subTest(
                "Testing ...",
                input=input,
                expected=expected,
            ):
                self.assertEqual(self.solver.part_two(input), expected)


class TestFolders(unittest.TestCase):
    def test_folder_size_with_only_files(self):
        d = Directory("d")
        files = (
            File(4060174, "j"),
            File(8033020, "d.log"),
            File(5626152, "d.ext"),
            File(7214296, "k"),
        )

        for file in files:
            d.add_file(file)

        self.assertEqual(d.size, 24933642)

    def test_folder_size_with_folders(self):
        a = Directory("a")
        e = Directory("e")
        z = Directory("z")

        z.add_file(File(20, "y"))

        e.add_file(File(584, "i"))
        e.add_dir(z)

        a.add_dir(e)

        files = (File(29116, "f"), File(2557, "g"), File(62596, "h.lst"))

        for file in files:
            a.add_file(file)

        self.assertEqual(a.size, 94873)
        self.assertEqual(e.size, 604)
        self.assertEqual(z.size, 20)


class TestFileSystem(unittest.TestCase):
    def setUp(self) -> None:
        self.fs = FileSystem()

    def test_pwd_and_cd(self):
        self.assertEqual(self.fs.pwd, "/")
        self.fs.current.add_dir(Directory("foo"))

        self.fs.cd("foo")
        self.assertEqual(repr(self.fs.current), "foo")
        self.assertEqual(self.fs.pwd, "/foo")

        self.fs.current.add_dir(Directory("bar"))
        self.fs.cd("bar")
        self.assertEqual(repr(self.fs.current), "bar")
        self.assertEqual(self.fs.pwd, "/foo/bar")

        with self.assertRaises(FileNotFoundError):
            self.fs.cd("baz")

        self.fs.cd("..")
        self.assertEqual(self.fs.pwd, "/foo")

        self.fs.cd("..")
        self.assertEqual(self.fs.pwd, "/")

        with self.assertRaises(FileNotFoundError):
            self.fs.cd("..")

    def test_ls(self):
        foo = Directory("foo")
        bar = Directory("bar")
        baz = File(100, "baz")
        cas = File(100, "cas")
        data = [foo, bar, baz, cas]

        self.fs.current.add_dir(foo)
        self.fs.current.add_dir(bar)
        self.fs.current.add_file(baz)
        self.fs.current.add_file(cas)

        self.assertEqual(self.fs.ls, data)
