import yaml


class YAMLModelLoader:
    """Load GPS institutional models from YAML files."""

    def load(self, path):
        with open(path, "r", encoding="utf-8") as file:
            return yaml.safe_load(file)
