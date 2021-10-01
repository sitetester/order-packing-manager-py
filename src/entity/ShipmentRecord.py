from src.entity.Container import Container
from src.entity.TotalVolume import TotalVolume


class ShipmentRecord:
    orderId: str
    totalVolume: TotalVolume
    containers: list[Container]

    def __init__(self, orderId: str, totalVolume: TotalVolume, containers: list[Container]):
        self.orderId = orderId
        self.totalVolume = totalVolume
        self.containers = containers

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            isEqual = True
            for i, c in enumerate(self.containers):
                if c != other.containers[i]:
                    isEqual = False

            return self.orderId == other.orderId and self.totalVolume == other.totalVolume and isEqual
        return False
