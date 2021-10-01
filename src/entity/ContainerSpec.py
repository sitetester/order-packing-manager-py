from src.entity import Dimensions


class ContainerSpec:
    containerType: str
    dimensions: Dimensions

    def __init__(self, containerType: str, dimensions: Dimensions):
        self.dimensions = dimensions
        self.containerType = containerType
