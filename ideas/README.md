# Ideas and hypotheses

This directory preserves possible directions separately from accepted design decisions. These are proposals, not requirements.

## Architecture and modeling
- **Universal component primitive:** represent domain operations, routing, transport, approval, evidence collection and whole systems using the same recursive abstraction.
- **Description plus contract:** freeform functionality text captures intent while typed configuration, inputs and outcomes provide machine-checkable boundaries.
- **Definitions versus instances:** reuse a single specification in many places with different configuration.
- **Explicit graph:** one-to-one wires make data flow auditable; multiple wires can represent fan-out without a new bus primitive.
- **Events as outcomes:** an emitted event is an occurrence on a typed output, avoiding a second foundational abstraction.

## LLM-centered workflow
- **Model tiering:** stronger models produce and critique architecture; cheaper models implement well-scoped components.
- **Component contracts as task packets:** each definition can supply implementation prompts, acceptance criteria and integration tests.
- **Hierarchical refinement:** expand a high-level system component into nested definitions and wiring, recursively.
- **Traceability:** preserve why components and connections exist, and connect implementation evidence back to contracts.
- **Validation before code:** test graph connectivity, type compatibility, missing definitions and unbound required inputs.

## Further explorations
- Versioned registries and dependency resolution.
- Execution semantics for synchronous, asynchronous and streaming outcomes.
- Explicit failure, cancellation, retry and compensation behavior.
- Policy and approval as ordinary composable components.
- Evidence/provenance as typed outputs.
- Human-readable visualization generated from the same IR.
- Bidirectional transformations between natural-language requirements, IR and code.

## Next experiments
1. Specify a minimal schema for definitions, instances and wires.
2. Make every reference in the example set resolvable.
3. Prototype static validation without choosing a runtime.
4. Compare one small workflow authored by a strong model and implemented by a cheaper model.
