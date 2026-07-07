class ReportGenerator:
    """Generate assessment reports from GPS findings."""

    def generate(self, findings):
        return {
            "finding_count": len(findings),
            "findings": findings,
        }
