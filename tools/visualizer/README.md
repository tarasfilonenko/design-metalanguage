# Browser visualizer

A zero-build, dependency-free HTML/JavaScript alternative to `tools/visualize/visualize.py`.

## Run

Serve the repository using GitHub Pages (deploy the root of `main`) and open:

`https://tarasfilonenko.github.io/design-metalanguage/tools/visualizer/?entry=../../examples/02-composition/main.json`

Or use any HTTP static server locally. Browsers generally block `fetch` for `file://` URLs.

## Resolution contract

- Entry point: `<example>/main.json` (a `component-instance`).
- Each `definition: "foo"` loads `<example>/components/foo.json`.
- Each definition's `id` must match its filename and reference.
- Nested instances resolve from the **same entry point folder**, not their parent's file.
- All required definitions belong to the example. No manifest, index.json, shared library or directory enumeration.
- Names are restricted to alphanumerics, hyphens and underscores, preventing path traversal.
- The resolver caches definitions, checks child instance IDs, validates wiring endpoint syntax and reports cycles.

The visualizer displays nested composition and wires textually. It does not execute components or implement a UI runtime. External entry-point URLs must allow browser CORS access.

## GitHub Pages

In repository Settings → Pages, select **Deploy from a branch**, branch **main**, folder **/(root)**. Pages publishing is separate from committing these files.
