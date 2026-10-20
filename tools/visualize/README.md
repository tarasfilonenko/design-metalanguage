# Component composition visualizer

Generate Mermaid flowcharts from self-contained examples. Requires Python 3; no third-party dependencies.

From the repository root:

```bash
python3 tools/visualize/visualize.py examples/02-composition --markdown > diagram.md
```

Without `--markdown`, output is raw Mermaid syntax. The tool recursively resolves local component definitions and shows composition and wires.
