class AssessmentRunner:
    """Coordinate GPS assessment execution."""

    def __init__(self, loader, repository, engine, reporter):
        self.loader = loader
        self.repository = repository
        self.engine = engine
        self.reporter = reporter

    def run(self, model_path):
        model = self.loader.load(model_path)
        findings = self.engine.evaluate(model)
        return self.reporter.generate(findings)
