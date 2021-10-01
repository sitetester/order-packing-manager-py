class Dimensions:
    unit: str
    width: int
    height: int
    length: int

    def __init__(self, unit: str, width: int, height: int, length: int):
        self.unit = unit
        self.width = width
        self.height = height
        self.length = length
