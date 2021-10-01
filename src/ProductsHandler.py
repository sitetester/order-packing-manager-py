from src.dimensionsHelper import DimensionsHelper
from src.entity import Product


class ProductsHandler:

    def getProductVolume(self, product: Product) -> int:
        return DimensionsHelper.getDimensionsVolume(product.dimensions)

    def getProductVolumePerOrderedQuantity(self, product: Product) -> int:
        return self.getProductVolume(product) * product.orderedQuantity
