import unittest
from props.palette import Palette
from shapes.point import Point
from shapes.square import Square


class FiguresTest(unittest.TestCase):
    def test_point(self):
        figure = {"type": "point", "x": 50, "y": 10, "color": "blue"}
        point = Point.build(figure)

        self.assertEqual(50, point.x)
        self.assertEqual(10, point.y)
        self.assertEqual("blue", point.color)

        figure = {"type": "point", "x": 50, "y": 10}
        point = Point.build(figure)

        self.assertEqual(None, point.color)

        figure = {"type": "point", "x": 50, "color": "blue"}
        self.assertRaises(ValueError, Point.build, figure)

    def test_square(self):
        figure = {"type": "square", "x": 50, "y": 10, "size": 10, "color": "blue"}
        square = Square.build(figure)

        self.assertEqual(50, square.x)
        self.assertEqual(10, square.y)
        self.assertEqual("blue", square.color)
        self.assertEqual(10, square.size)

        figure = {"type": "square", "x": 50, "y": 10}
        self.assertRaises(ValueError, Square.build, figure)

if __name__ == '__main__':
    unittest.main()