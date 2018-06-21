class Shape:
    @staticmethod
    def validate(obj, required_args):
        for arg in required_args:
            if arg not in obj or obj[arg] is None:
                raise ValueError("invalid json")