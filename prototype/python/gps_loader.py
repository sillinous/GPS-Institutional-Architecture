import yaml


def load_gps_model(path):
    """Load a GPS institutional model from YAML."""
    with open(path, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)


if __name__ == "__main__":
    model = load_gps_model("../sample-data/example-enterprise.yaml")
    print(model)
