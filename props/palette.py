import re
from ast import literal_eval


class Palette:
    def __init__(self, colors):
        self._colors = {}

        for k, v in colors.items():
            if Palette.is_valid(v):
                self._colors[k] = v

    def get_color(self, color):
        if color is None:
            return None

        if self.has_color(color):
            return self._colors[color]

        if Palette.is_rgb(color):
            return literal_eval(color)

        if Palette.is_hex(color):
            return color

        raise ValueError("invalid color")

    def has_color(self, color):
        return color in self._colors

    @staticmethod
    def is_valid(color):
        if not color:
            return False

        if Palette.is_hex(color) or Palette.is_rgb(color):
            return True

        return False

    @staticmethod
    def is_rgb(color):
        return bool(re.match('\([0-9]{1,3},[0-9]{1,3},[0-9]{1,3}\)', color))

    @staticmethod
    def is_hex(color):
        return bool(re.match('#[a-fA-F0-9]{6}', color))