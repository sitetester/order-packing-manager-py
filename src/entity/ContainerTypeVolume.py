class ContainerTypeVolume:
    containerType: str
    volume: int

    def __init__(self, containerType: str, volume: int):
        self.containerType = containerType
        self.volume = volume
