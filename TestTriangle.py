import unittest
from ProdactionCode.Triangle import Triangle


class TestTriangle(unittest.TestCase):
    def setUp(self):
        self.normalSides = [3, 4, 5]
        self.negativeSides = [4, -1, 3]
        self.incorrectSides = [2, 10, 4]
        self.areaNormalSides = 6

    def test_set_normal_sides(self):
        triangle = Triangle(self.normalSides[0], self.normalSides[1], self.normalSides[2])
        self.assertCountEqual(self.normalSides, [triangle.a, triangle.b, triangle.c])

    @unittest.expectedFailure
    def test_set_negative_sides(self):
        self.assertRaises(TypeError, Triangle(self.negativeSides[0], self.negativeSides[1], self.negativeSides[2]))

    @unittest.expectedFailure
    def test_set_incorrect_sides(self):
        self.assertRaises(ValueError, Triangle(self.incorrectSides[0], self.incorrectSides[1], self.incorrectSides[2]))

    def test_area_triangle(self):
        triangle = Triangle(self.normalSides[0], self.normalSides[1], self.normalSides[2])
        self.assertEqual(self.areaNormalSides, triangle.area())
