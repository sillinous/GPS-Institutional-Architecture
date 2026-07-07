def assess_model(model):
    """Evaluate a GPS institutional model."""
    findings = []

    for capability in model.get("capabilities", []):
        maturity = capability.get("maturity", 0)
        if maturity < 3:
            findings.append({
                "capability": capability.get("name"),
                "finding": "Capability improvement opportunity identified"
            })

    return findings


if __name__ == "__main__":
    print("GPS assessment engine ready")
