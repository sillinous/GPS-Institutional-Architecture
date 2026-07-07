class Capability:
    """Represents an institutional capability."""

    def __init__(self, identifier, name, maturity=0):
        self.identifier = identifier
        self.name = name
        self.maturity = maturity
