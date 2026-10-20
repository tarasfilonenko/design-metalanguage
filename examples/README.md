# Examples

Each example is a self-contained folder. `main.json` is the entry point: a configured root component instance referencing a definition by its `definition` ID. `components/` contains all definitions needed by that example, including nested composite definitions. References resolve by definition `id` within the local `components/` folder.

- `01-transform/`: one atomic component.
- `02-composition/`: composite greeting pipeline.
- `03-approval-workflow/`: draft, evidence, approval and publishing.

These examples demonstrate the proposed structure; the schema and execution semantics are not yet finalized.
