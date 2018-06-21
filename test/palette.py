import unittest
from props.palette import Palette


class PaletteTest(unittest.TestCase):
    def test_rgb(self):
        self.assertEqual(True, Palette.is_rgb("(255,255,255)"))
        self.assertEqual(False, Palette.is_rgb("(255,255)"))
        self.assertEqual(False, Palette.is_rgb("(255,255,-1)"))

    def test_hex(self):
        self.assertEqual(True, Palette.is_hex("#DEAD00"))
        self.assertEqual(True, Palette.is_hex("#BEEF00"))
        self.assertEqual(False, Palette.is_hex("#XDDDDD"))

        self.assertEqual(True, Palette.is_valid("#ABCDEF"))
        self.assertEqual(True, Palette.is_valid("(123,123,123)"))

    def test_get_color(self):
        colors = {"white": "(255,255,255)", "green": "#00ff00"}
        palette = Palette(colors)

        self.assertRaises(ValueError, palette.get_color, "red")
        self.assertEqual((123, 123, 123), palette.get_color("(123,123,123)"))

if __name__ == '__main__':
    unittest.main()