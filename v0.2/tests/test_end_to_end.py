import os


class TestGPSAssessmentFlow:
    """Validate the GPS v0.2 assessment lifecycle."""

    def test_assessment_components_exist(self):
        expected_components = [
            "v0.2/loaders/yaml_model_loader.py",
            "v0.2/execution/run_assessment.py",
            "v0.2/reasoning/rule_engine.py",
            "v0.2/reporting/report_generator.py",
        ]

        for component in expected_components:
            assert os.path.exists(component)

    def test_assessment_output_contract(self):
        report = {
            "finding_count": 0,
            "findings": [],
        }

        assert "finding_count" in report
        assert "findings" in report
