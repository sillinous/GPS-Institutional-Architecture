from python.gps_loader import load_gps_model


def test_model_loads():
    model = load_gps_model("sample-data/example-enterprise.yaml")
    assert "institution" in model
