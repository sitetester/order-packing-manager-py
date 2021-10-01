class TotalVolume:
    unit: str
    value: int

    def __init__(self, unit: str, value: int):
        self.unit = unit
        self.value = value

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.unit == other.unit and self.value == other.value
        return False
