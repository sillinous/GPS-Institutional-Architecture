import json
from jsonschema import validate


def validate_model(model, schema_path):
    """Validate a GPS model against a JSON schema."""
    with open(schema_path, "r", encoding="utf-8") as file:
        schema = json.load(file)

    validate(instance=model, schema=schema)
    return True


if __name__ == "__main__":
    print("GPS schema validator ready")
