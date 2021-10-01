from src.entity import Dimensions


class DimensionsHelper:

    @staticmethod
    def getDimensionsVolume(dimensions: Dimensions) -> int:
        return dimensions.width * dimensions.height * dimensions.length
