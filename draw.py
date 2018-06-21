from PIL import Image, ImageDraw

from shapes.point import Point
from shapes.circle import Circle
from shapes.polygon import Polygon
from shapes.rectangle import Rectangle
from shapes.square import Square


class Drawer:
    def __init__(self, screen, figures, palette):
        self._palette = palette
        self._screen = screen
        self._im = Image.new("RGB", (screen.width, screen.height), self._palette.get_color(screen.bg_color))
        self._draw = ImageDraw.Draw(self._im)
        self._figures = figures

    def draw(self):
        color = self._palette.get_color(self._screen.fg_color)

        for figure in self._figures:
            if figure.color is not None:
                color = self._palette.get_color(figure.color)

            if isinstance(figure, Point):
                self._draw.point((figure.x, figure.y), fill=color)
            elif isinstance(figure, Polygon):
                self._draw.polygon(figure.points, fill=color)
            elif isinstance(figure, Circle):
                self._draw.ellipse([figure.x - figure.radius,
                                    figure.y - figure.radius,
                                    figure.x + figure.radius,
                                    figure.y + figure.radius],
                                   color)
            elif isinstance(figure, Rectangle):
                self._draw.rectangle([figure.x - figure.width / 2,
                                      figure.y - figure.height / 2,
                                      figure.x + figure.width / 2,
                                      figure.y + figure.height / 2],
                                     fill=color)
            elif isinstance(figure, Square):
                self._draw.rectangle([figure.x - figure.size / 2,
                                      figure.y - figure.size / 2,
                                      figure.x + figure.size / 2,
                                      figure.y + figure.size / 2],
                                     fill=color)

        self._im.show()

    def save(self, name):
        self._im.save(name, "JPEG")