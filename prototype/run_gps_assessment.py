from python.gps_loader import load_gps_model
from python.assessment_engine import assess_model
from python.report_generator import generate_report


if __name__ == "__main__":
    model = load_gps_model("sample-data/example-enterprise.yaml")
    findings = assess_model(model)
    report = generate_report(model.get("institution", {}), findings)
    print(report)
