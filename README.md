# Design Metalanguage

An extensible, LLM-oriented component intermediate representation (IR) for describing, composing, reviewing and implementing systems.

## Vision
A stronger model designs architectures as structured component graphs; less expensive models implement individual components against explicit contracts.

## Principles
- Components are the universal modeling primitive, including whole systems and supporting capabilities.
- Component definitions are reusable contracts; instances configure and place definitions in a design.
- Definitions include freeform functionality descriptions and typed configuration, inputs, and outcomes.
- Components can recursively contain other components.
- Composition uses explicit, one-to-one wiring between typed endpoints.
- Events are typed output occurrences, not a separate core entity.
- Transport, routing, evidence, and approvals can themselves be components.

## Contents
- [Core model](docs/core-model.md)
- [Decisions and open questions](docs/decisions.md)
- [Idea backlog](ideas/README.md)
- [Examples](examples/)

## Status
Exploratory design. JSON examples are illustrative, not a frozen schema or implemented validator.
