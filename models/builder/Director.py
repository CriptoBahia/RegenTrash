from .Builder import Builder


class Director:
    """
    The Director is only responsible for executing the building steps in a
    particular sequence. It is helpful when producing products according to a
    specific order or configuration. Strictly speaking, the Director class is
    optional, since the client can control builders directly.
    """

    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    """
    The Director can construct several product variations using the same
    building steps.
    """


    def build_full_featured_product(self) -> None:
        self.builder.produce_type()
        self.builder.produce_position()
        self.builder.produce_speed()
        self.builder.produce_surface()
        self.builder.produce_rect()
        self.builder.produce_direction()
         