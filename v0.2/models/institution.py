class Institution:
    """Represents an institutional entity in GPS."""

    def __init__(self, identifier, name):
        self.identifier = identifier
        self.name = name
        self.capabilities = []

    def add_capability(self, capability):
        self.capabilities.append(capability)
