class Square:
    required_args = ["x", "y", "size"]

    def __init__(self, x, y, size, color = None):
        self.x = x
        self.y = y
        self.size = size
        self.color = color

    @staticmethod
    def build(figure):
        for arg in Square.required_args:
            if arg not in figure or figure[arg] is None:
                raise ValueError("invalid json")

        color = figure["color"] if "color" in figure else None

        return Square(figure["x"], figure["y"], figure["size"], color)
