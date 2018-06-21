class Polygon:
    required_args = ["points"]

    def __init__(self, points, color = None):
        self.points = points
        self.color = color

    @staticmethod
    def build(figure):
        for arg in Polygon.required_args:
            if arg not in figure or figure[arg] is None:
                raise ValueError("invalid json")

        color = figure["color"] if "color" in figure else None

        return Polygon(list(map(lambda x: tuple(x), figure["points"])), color)
