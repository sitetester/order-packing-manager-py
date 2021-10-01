from src.dimensionsHelper import DimensionsHelper
from src.entity.ContainerSpec import ContainerSpec
from src.entity.ContainerTypeVolume import ContainerTypeVolume


class ContainersHandler:
    __containerSpecs: list[ContainerSpec]

    def __init__(self, containerSpecs: list[ContainerSpec]):
        self.__containerSpecs = containerSpecs

    def getContainers(self) -> list[ContainerSpec]:
        return self.__containerSpecs

    def getContainerTypeVolume(self, containerType: str) -> int:
        containerSpec = list(
            filter(lambda containerSpecTemp: containerSpecTemp.containerType == containerType, self.getContainers())
        )[0]

        return self.getContainerVolume(containerSpec)

    def getContainerTypesVolume(self) -> list[ContainerTypeVolume]:
        containerTypesVolume = list[ContainerTypeVolume]()

        for containerSpec in self.__containerSpecs:
            containerTypesVolume.append(
                ContainerTypeVolume(containerSpec.containerType, self.getContainerVolume(containerSpec))
            )

        return containerTypesVolume

    @staticmethod
    def getContainerVolume(containerSpec: ContainerSpec) -> int:
        return DimensionsHelper.getDimensionsVolume(containerSpec.dimensions)
