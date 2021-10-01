import unittest

from src.entity.Container import Container
from src.entity.ContainerSpec import ContainerSpec
from src.entity.ContainingProduct import ContainingProduct
from src.entity.Dimensions import Dimensions
from src.entity.OrderRequest import OrderRequest
from src.entity.Product import Product
from src.entity.ShipmentRecord import ShipmentRecord
from src.entity.TotalVolume import TotalVolume
from src.orderHandler import OrdersHandler


class TestOrder(unittest.TestCase):
    def test_order(self):
        """
        Given a small order, pack it into a single container
        """

        containerSpecs = list[ContainerSpec]()

        containerSpecs.append(ContainerSpec("Cardboard A", Dimensions("centimeter", 30, 30, 30)))
        containerSpecs.append(ContainerSpec("Cardboard B", Dimensions("centimeter", 10, 20, 20)))

        ordersHandler = OrdersHandler(containerSpecs)

        products: list[Product] = list[Product]()
        products.append(Product("PRODUCT-001", "GOOD FORTUNE COOKIES", 9, Dimensions("centimeter", 10, 10, 30), 13.4))
        orderRequest = OrderRequest("ORDER-001", products)

        containingProducts = list[ContainingProduct]()
        containingProducts.append(ContainingProduct("PRODUCT-001", 9))

        containers = list[Container]()
        containers.append(Container("Cardboard A", containingProducts))

        expectedShipmentRecord = ShipmentRecord("ORDER-001", TotalVolume("cubic centimeter", 27000), containers)
        self.assertEqual(expectedShipmentRecord, ordersHandler.packOrder(orderRequest))


if __name__ == '__main__':
    unittest.main()
