"""GPS v0.2 command line assessment interface."""

import argparse
import json

from loaders.yaml_model_loader import YAMLModelLoader
from loaders.model_converter import ModelConverter
from reasoning.rule_engine import RuleEngine
from reasoning.example_rules import capability_maturity_rule
from reporting.report_generator import ReportGenerator


def build_parser():
    parser = argparse.ArgumentParser(description="Run a GPS institutional assessment")
    parser.add_argument(
        "--model",
        default="v0.2/examples/enterprise-model-v2.yaml",
        help="Path to institutional model YAML file",
    )
    return parser


def run_assessment(model_path):
    loader = YAMLModelLoader()
    converter = ModelConverter()
    engine = RuleEngine([capability_maturity_rule])
    reporter = ReportGenerator()

    raw_model = loader.load(model_path)
    institution = converter.convert(raw_model)
    findings = engine.evaluate(institution)

    return reporter.generate(findings)


def main():
    parser = build_parser()
    args = parser.parse_args()

    report = run_assessment(args.model)
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
