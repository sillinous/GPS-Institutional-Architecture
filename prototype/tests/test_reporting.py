from python.report_generator import generate_report


def test_report_generation():
    report = generate_report(
        {"name": "Example Enterprise"},
        [{"capability": "Decision Intelligence", "finding": "Improvement needed"}]
    )

    assert "Example Enterprise" in report
    assert "Decision Intelligence" in report
