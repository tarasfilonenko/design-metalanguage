# Decisions and questions

## Agreed direction
1. Universal recursive components, including systems and infrastructure functions.
2. Separate reusable definitions from configured instances.
3. Freeform functionality descriptions alongside typed contracts.
4. Explicit one-to-one wires between endpoints.
5. Typed outputs/occurrences model events; no distinct event primitive.
6. Architecture can be authored by stronger LLMs and delegated for implementation to cheaper models.

## Open questions
- Canonical serialization (JSON, YAML, or purpose-built notation)?
- Type system and compatibility/subtyping rules?
- Sync versus async execution, streams, retries and errors?
- How should outcomes distinguish values, failures and emitted events?
- How are component definitions versioned and resolved?
- How are invariants, evidence, approval and security policies expressed?
- How can examples be checked automatically and compiled into implementation tasks?

## Non-goals
No premature runtime, orchestrator, programming-language binding or validator commitment.
