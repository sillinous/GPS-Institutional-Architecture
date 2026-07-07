def generate_report(institution, findings):
    """Generate a simple GPS assessment report."""
    lines = [
        "GPS Assessment Report",
        "",
        f"Institution: {institution.get('name', 'Unknown')}",
        "",
        "Findings:"
    ]

    for finding in findings:
        lines.append(
            f"- {finding.get('capability')}: {finding.get('finding')}"
        )

    return "\n".join(lines)


if __name__ == "__main__":
    print("GPS report generator ready")
