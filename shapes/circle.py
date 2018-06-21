class Circle:
    required_args = ["x", "y", "radius"]

    def __init__(self, x, y, radius, color = None):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    @staticmethod
    def build(figure):
        for arg in Circle.required_args:
            if arg not in figure or figure[arg] is None:
                raise ValueError("invalid json")

        color = figure["color"] if "color" in figure else None

        return Circle(figure["x"], figure["y"], figure["radius"], color)
