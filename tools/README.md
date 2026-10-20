# Tools

Utilities for inspecting and validating the design metalanguage.

## Visualize a component and its composition

`visualize.py` is a Python 3 standard-library CLI that reads an example's `main.json`, resolves definitions in its local `components/` directory, and generates a Mermaid flowchart.

```bash
python3 tools/visualize.py examples/02-composition > composition.mmd
```

Paste the output into a Mermaid-enabled Markdown viewer, or wrap it in a fenced `mermaid` block. You can also write directly to a Markdown file:

```bash
python3 tools/visualize.py examples/03-approval-workflow --markdown > approval-diagram.md
```

The diagram shows the root instance, nested component instances, their definition IDs and explicit wires. Composite components are expanded recursively. The tool reports unresolved definitions, malformed wires and recursive definition cycles rather than silently ignoring them.

No external dependencies. The diagram is a structural visualization, not a runtime execution graph.
