from src.entity.ContainingProduct import ContainingProduct


class Container:
    containerType: str
    containingProducts: list[ContainingProduct]

    def __init__(self, containerType: str, containingProducts: list[ContainingProduct]):
        self.containerType = containerType
        self.containingProducts = containingProducts

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            isEqual = True
            for i, cp in enumerate(self.containingProducts):
                otherProd = other.containingProducts[i]
                if cp != otherProd:
                    isEqual = False

            return self.containerType == other.containerType and isEqual
        return False
