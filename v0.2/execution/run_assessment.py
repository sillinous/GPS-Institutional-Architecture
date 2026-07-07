class AssessmentRunner:
    """Coordinate GPS assessment execution."""

    def __init__(self, loader, converter, repository, engine, reporter):
        self.loader = loader
        self.converter = converter
        self.repository = repository
        self.engine = engine
        self.reporter = reporter

    def run(self, model_path):
        raw_model = self.loader.load(model_path)
        model = self.converter.convert(raw_model)

        self.repository.save(model)

        findings = self.engine.evaluate(model)
        return self.reporter.generate(findings)
