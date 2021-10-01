class ContainingProduct:
    id: str
    quantity: int

    def __init__(self, id: str, quantity: int):
        self.id = id
        self.quantity = quantity

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.id == other.id and self.quantity == other.quantity
        return False
