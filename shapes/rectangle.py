class Rectangle:
    required_args = ["x", "y", "width", "height"]

    def __init__(self, x, y, width, height, color = None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    @staticmethod
    def build(figure):
        for arg in Rectangle.required_args:
            if arg not in figure or figure[arg] is None:
                raise ValueError("invalid json")

        color = figure["color"] if "color" in figure else None

        return Rectangle(figure["x"], figure["y"], figure["width"], figure["height"], color)
