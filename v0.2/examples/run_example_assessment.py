"""Run a GPS v0.2 example assessment."""

from reasoning.rule_engine import RuleEngine
from reasoning.example_rules import capability_maturity_rule
from reporting.report_generator import ReportGenerator
from loaders.yaml_model_loader import YAMLModelLoader
from loaders.model_converter import ModelConverter


def run():
    loader = YAMLModelLoader()
    converter = ModelConverter()
    engine = RuleEngine([capability_maturity_rule])
    reporter = ReportGenerator()

    raw_model = loader.load("v0.2/examples/enterprise-model-v2.yaml")
    institution = converter.convert(raw_model)

    findings = engine.evaluate(institution)
    return reporter.generate(findings)


if __name__ == "__main__":
    print(run())
