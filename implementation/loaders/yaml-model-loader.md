# GPS YAML Model Loader Design

## Purpose
Define how GPS YAML instance artifacts are loaded into a validated institutional model.

## Input

Existing GPS YAML artifacts:

- Institution definitions
- Capability definitions
- Actor definitions
- Decision definitions
- Outcome definitions
- Resource definitions
- Knowledge definitions
- Transformation definitions

## Processing Flow

1. Discover model files.
2. Parse YAML content.
3. Validate against GPS schemas.
4. Resolve entity references.
5. Build institutional graph.
6. Pass model to assessment engine.

## Output

A validated GPS institutional model ready for analysis.
