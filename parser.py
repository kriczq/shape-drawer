import json
from props.palette import Palette
from props.screen import Screen

from shapes.point import Point
from shapes.circle import Circle
from shapes.polygon import Polygon
from shapes.rectangle import Rectangle
from shapes.square import Square


class Parser:
    def __init__(self, path):
        with open(path, 'r') as fp:
            obj = json.load(fp)

            self.palette = Palette(obj["Palette"])

            if ("width" or "height" or "bg_color" or "fg_color") not in obj["Screen"]:
                raise ValueError("incorrect screen")

            self.screen = Screen(obj["Screen"]["width"], obj["Screen"]["height"], obj["Screen"]["bg_color"], obj["Screen"]["fg_color"])
            self.figures = []

            for figure in obj["Figures"]:
                self.figures += [Parser.build_figure(figure)]

    @staticmethod
    def build_figure(figure):
        if figure["type"] == "point":
            return Point.build(figure)

        if figure["type"] == "circle":
            return Circle.build(figure)

        if figure["type"] == "polygon":
            return Polygon.build(figure)

        if figure["type"] == "rectangle":
            return Rectangle.build(figure)

        if figure["type"] == "square":
            return Square.build(figure)

        raise ValueError("incorrect type")
