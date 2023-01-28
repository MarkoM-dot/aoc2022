import unittest

from aoc2022.day9 import DayNine, Rope, Vector

part_one_data = (("R 4\nU 4\nL 3\nD 1\nR 4\nD 1\nL 5\nR 2\n", "13"),)
part_two_data = (("R 4\nU 4\nL 3\nD 1\nR 4\nD 1\nL 5\nR 2\n", ""),)


class TestDayNine(unittest.TestCase):
    def setUp(self) -> None:
        self.solver = DayNine()

    @unittest.skip("not ready yet...")
    def test_part_one(self):
        for input, expected in part_one_data:
            with self.subTest(
                "Testing first start-of-packet marker part one...",
                input=input,
                expected=expected,
            ):
                self.assertEqual(self.solver.part_one(input), expected)

    @unittest.skip("Not ready yet...")
    def test_two_one(self):
        for input, expected in part_two_data:
            with self.subTest(
                "Testing ...",
                input=input,
                expected=expected,
            ):
                self.assertEqual(self.solver.part_two(input), expected)


class TestVector(unittest.TestCase):
    def setUp(self) -> None:
        self.v = Vector()
        self.w = Vector()

    def test_vectors_are_touching(self):
        self.assertTrue(self.v.is_touching(self.w))
        self.assertTrue(self.v.is_touching(self.w + Vector(1, 1)))
        self.assertTrue(self.v.is_touching(self.w + Vector(-1, -1)))
        self.assertTrue(self.v.is_touching(self.w + Vector(0, -1)))
        self.assertTrue(self.v.is_touching(self.w + Vector(-1, 0)))

        self.assertFalse(self.v.is_touching(self.w + Vector(0, 2)))
        self.assertFalse(self.v.is_touching(self.w + Vector(2, 0)))
        self.assertFalse(self.v.is_touching(self.w + Vector(-2, 0)))
        self.assertFalse(self.v.is_touching(self.w + Vector(0, -2)))
        self.assertFalse(self.v.is_touching(self.w + Vector(8, -8)))

    def test_vectors_can_follow(self):
        self.assertEqual(self.v.follow(self.w), Vector(0, 0))

        moving_vec = self.v + Vector(1, 1)
        self.assertEqual(self.w.follow(moving_vec), Vector(0, 0))

        moving_vec += Vector(1, 1)
        self.assertEqual(self.w.follow(moving_vec), Vector(1, 1))


class TestRope(unittest.TestCase):
    def setUp(self) -> None:
        self.rope = Rope()

    def test_move(self):
        self.rope.move("R", 3)
        self.assertEqual(self.rope.head, Vector(3, 0))

        self.rope.move("U", 2)
        self.assertEqual(self.rope.head, Vector(3, 2))
