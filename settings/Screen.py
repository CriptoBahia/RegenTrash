from .Config import Config


class Screen:
    def __init__(self, config = Config) -> None:
        self.surface = config.surface
        self.cellSize = config.cellSize
