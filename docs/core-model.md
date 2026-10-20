# Conceptual model (draft)

## Definition
A reusable component specification with an identifier, a natural-language `functionality` description, typed `configuration`, `inputs`, and `outcomes`. A definition may declare nested component instances and explicit wires.

## Instance
A placement of a definition within a design, with an instance identifier and bound configuration. Multiple instances may reference the same definition.

## Composition
A composite definition contains instances and wires. Each wire connects one source outcome to one destination input. Fan-out can be represented by multiple distinct wires; implicit buses are not part of the core model.

## Events
An event is an occurrence/value emitted through a typed outcome. It does not require an independent foundational schema entity.

## Recursive scope
A whole application, approval gate, router, evidence collector, transport adapter, or single operation can be a component.

## Types
Type syntax, compatibility, versioning, cardinality, execution semantics, and lifecycle are undecided. Examples use JSON-style type labels for readability.
