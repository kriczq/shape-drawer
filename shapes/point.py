class Point:
    required_args = ["x", "y"]

    def __init__(self, x, y, color = None):
        self.x = x
        self.y = y
        self.color = color

    @staticmethod
    def build(figure):
        for arg in Point.required_args:
            if arg not in figure or figure[arg] is None:
                raise ValueError("invalid json")

        color = figure["color"] if "color" in figure else None

        return Point(figure["x"], figure["y"], color)
