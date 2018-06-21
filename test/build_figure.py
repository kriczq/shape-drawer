import unittest
from props.palette import Palette
from parser import Parser
from shapes.point import Point


class ParserTest(unittest.TestCase):
    def test_build_figure(self):
        figure = {"type": "point", "x": 50, "y": 10, "color": "blue"}
        self.assertEqual(True, isinstance(Parser.build_figure(figure), Point))

        figure = {"type": "cat", "x": 50, "y": 10, "color": "blue"}
        self.assertRaises(ValueError, Parser.build_figure, figure)


if __name__ == '__main__':
    unittest.main()
