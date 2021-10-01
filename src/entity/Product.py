from src.entity.Dimensions import Dimensions


class Product:
    id: str
    name: str
    orderedQuantity: int
    dimensions: Dimensions
    unitPrice: float

    def __init__(self, id: str, name: str, orderedQuantity: int, dimensions: Dimensions, unitPrice: float):
        self.id = id
        self.name = name
        self.orderedQuantity = orderedQuantity
        self.dimensions = dimensions
        self.unitPrice = unitPrice
