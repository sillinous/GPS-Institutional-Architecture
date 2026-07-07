class Relationship:
    """Represents a connection between GPS entities."""

    def __init__(self, source, relation_type, target):
        self.source = source
        self.relation_type = relation_type
        self.target = target
