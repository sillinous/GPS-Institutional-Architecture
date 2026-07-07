from validation.schema_validator import validate_model


def test_schema_validator_exists():
    assert callable(validate_model)
