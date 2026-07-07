class InMemoryRepository:
    """Simple in-memory persistence boundary for GPS models."""

    def __init__(self):
        self._entities = {}

    def save(self, entity):
        identifier = getattr(entity, "identifier", None)
        if identifier is None:
            raise ValueError("Entity must have an identifier")
        self._entities[identifier] = entity

    def get(self, identifier):
        return self._entities.get(identifier)

    def all(self):
        return list(self._entities.values())
