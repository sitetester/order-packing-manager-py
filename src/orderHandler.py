from src.ContainersHandler import ContainersHandler
from src.ProductsHandler import ProductsHandler
from src.entity.Container import Container
from src.entity.ContainerSpec import ContainerSpec
from src.entity.ContainingProduct import ContainingProduct
from src.entity.OrderRequest import OrderRequest
from src.entity.Product import Product
from src.entity.ShipmentRecord import ShipmentRecord
from src.entity.TotalVolume import TotalVolume


class OrdersHandler:
    __containersHandler: ContainersHandler
    __productsHandler: ProductsHandler

    def __init__(self, containerSpecs: list[ContainerSpec]):
        self.__containersHandler = ContainersHandler(containerSpecs)
        self.__productsHandler = ProductsHandler()

    def packOrder(self, orderRequest: OrderRequest) -> ShipmentRecord:
        self.__checkOrderExecutable(orderRequest)
        containers = self.getContainers(orderRequest)

        return ShipmentRecord(
            orderRequest.id,
            TotalVolume("cubic centimeter", self.getTotalVolume(containers)),
            containers
        )

    def __checkOrderExecutable(self, orderRequest: OrderRequest):
        containerTypesVolume = self.__containersHandler.getContainerTypesVolume()

        for product in orderRequest.products:
            productVolume = self.__productsHandler.getProductVolume(product)

            timesProductVolumeGreater = 0
            for containerTypeVolume in containerTypesVolume:
                if productVolume > containerTypeVolume.volume:
                    timesProductVolumeGreater += 1

            if timesProductVolumeGreater == len(containerTypesVolume):
                msg = f'Order can\'t be executed, since one of it\'s product(s) ({product.id})'
                msg += 'volume exceeds available containers volume.'
                raise Exception(msg)

    def getContainers(self, orderRequest: OrderRequest):
        containers = list[Container]()
        availableContainers = self.__containersHandler.getContainers()

        for product in orderRequest.products:
            quantityAdded = 0
            i = 0
            while i <= len(availableContainers):
                containerSpec = availableContainers[i]
                containingProducts = list[ContainingProduct]()
                if self.canStoreProduct(containerSpec, product):
                    if self.canStoreProductPerOrderedQuantity(containerSpec, product):
                        containers.append(Container(containerSpec.containerType,
                                                    self.addToContainingProducts(containingProducts, product.id,
                                                                                 product.orderedQuantity)
                                                    ))
                        quantityAdded += product.orderedQuantity
                        break  # no need to check in next container
                    else:
                        howManyCanBeStored = self.howManyCanBeStored(containerSpec, product)
                        containers.append(Container(containerSpec.containerType,
                                                    self.addToContainingProducts(containingProducts, product.id,
                                                                                 howManyCanBeStored)
                                                    ))
                        quantityAdded += howManyCanBeStored

            diff = product.orderedQuantity - quantityAdded
            if diff > 0:
                # same container could be used multiple times
                containers = self.reuseSameContainer(diff, containers)

        return containers

    def canStoreProduct(self, containerSpec: ContainerSpec, product: Product) -> bool:
        return self.__containersHandler.getContainerVolume(containerSpec) \
               >= self.__productsHandler.getProductVolume(product)

    def canStoreProductPerOrderedQuantity(self, containerSpec: ContainerSpec, product: Product) -> bool:
        return self.__containersHandler.getContainerVolume(containerSpec) \
               >= self.__productsHandler.getProductVolumePerOrderedQuantity(product)

    @staticmethod
    def addToContainingProducts(containingProducts: list[ContainingProduct], id: str, quantity: int) \
            -> list[ContainingProduct]:
        containingProducts.append(ContainingProduct(id, quantity))
        return containingProducts

    def howManyCanBeStored(self, containerSpec: ContainerSpec, product: Product) -> int:
        containerVolume = self.__containersHandler.getContainerVolume(containerSpec)
        productVolume = self.__productsHandler.getProductVolume(product)
        adjustableVolume = productVolume

        quantity = 0
        while adjustableVolume <= containerVolume:
            adjustableVolume += productVolume
            quantity += 1

        return quantity

    @staticmethod
    def reuseSameContainer(howManyTimes: int, containers: list[Container]) -> list[Container]:
        container = containers[0]
        i = 0
        while i < howManyTimes:
            containers.append(container)

        return containers

    def getTotalVolume(self, containers: list[Container]):
        totalVolume = 0
        for container in containers:
            totalVolume += self.__containersHandler.getContainerTypeVolume(container.containerType)
        return totalVolume
