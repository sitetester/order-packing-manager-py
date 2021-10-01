from src.entity.Product import Product


class OrderRequest:
    id: str
    products: list[Product]

    def __init__(self, id: str, products: list[Product]):
        self.id = id
        self.products = products
