from python.assessment_engine import assess_model


def test_assessment_detects_low_maturity():
    model = {
        "capabilities": [
            {"name": "Example Capability", "maturity": 1}
        ]
    }

    findings = assess_model(model)
    assert len(findings) == 1
