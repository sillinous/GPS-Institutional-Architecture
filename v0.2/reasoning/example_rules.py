def capability_maturity_rule(institution):
    """Example rule identifying capabilities needing improvement."""

    findings = []

    for capability in getattr(institution, "capabilities", []):
        if capability.maturity < 3:
            findings.append({
                "observation": f"Capability {capability.name} maturity is below target.",
                "capability": capability.name,
                "severity": "medium",
                "recommendation": "Develop a capability improvement plan.",
            })

    return findings
