class RuleEngine:
    """Evaluate GPS institutional models using assessment rules."""

    def __init__(self, rules=None):
        self.rules = rules or []

    def evaluate(self, model):
        findings = []

        for rule in self.rules:
            result = rule(model)
            if result:
                findings.append(result)

        return findings
