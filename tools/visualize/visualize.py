#!/usr/bin/env python3
"""Render an example's component composition as a Mermaid flowchart."""
import argparse
import json
import re
import sys
from pathlib import Path


def load_example(folder):
    root = json.loads((folder / "main.json").read_text(encoding="utf-8"))
    definitions = {}
    for path in sorted((folder / "components").glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        if data.get("kind") != "component-definition" or not data.get("id"):
            raise ValueError(f"Invalid component definition: {path}")
        if data["id"] in definitions:
            raise ValueError(f"Duplicate definition ID: {data['id']}")
        definitions[data["id"]] = data
    if root.get("kind") != "component-instance" or not root.get("definition"):
        raise ValueError("main.json must be a component-instance with a definition")
    return root, definitions


def mermaid(root, definitions):
    lines = ["flowchart LR"]
    count = 0

    def node(label, shape="rect"):
        nonlocal count
        count += 1
        identifier = f"n{count}"
        escaped = str(label).replace("\\", "\\\\").replace('"', "&quot;").replace("\n", " ")
        lines.append(f'  {identifier}["{escaped}"]')
        return identifier

    def expand(instance, stack):
        definition_id = instance["definition"]
        if definition_id not in definitions:
            raise ValueError(f"Unresolved definition: {definition_id}")
        if definition_id in stack:
            raise ValueError("Recursive definition cycle: " + " -> ".join(stack + [definition_id]))
        definition = definitions[definition_id]
        current = node(f"{instance.get('id', definition_id)} : {definition_id}")
        children = {}
        for child in definition.get("components", []):
            child_id = child.get("id")
            if not child_id or child_id in children:
                raise ValueError(f"Missing or duplicate child instance ID in {definition_id}")
            children[child_id] = expand(child, stack + [definition_id])
            lines.append(f"  {current} -. contains .-> {children[child_id]}")
        for wire in definition.get("wires", []):
            source = wire.get("from", "")
            target = wire.get("to", "")
            def endpoint(value):
                if value.startswith("inputs.") or value.startswith("outcomes."):
                    return current
                prefix = value.split(".", 1)[0]
                if prefix not in children:
                    raise ValueError(f"Unknown endpoint in {definition_id}: {value}")
                return children[prefix]
            if not re.fullmatch(r"[A-Za-z0-9_-]+\.(inputs|outcomes)\.[A-Za-z0-9_-]+|(?:inputs|outcomes)\.[A-Za-z0-9_-]+", source):
                raise ValueError(f"Malformed wire source: {source}")
            if not re.fullmatch(r"[A-Za-z0-9_-]+\.(inputs|outcomes)\.[A-Za-z0-9_-]+|(?:inputs|outcomes)\.[A-Za-z0-9_-]+", target):
                raise ValueError(f"Malformed wire target: {target}")
            label = f"{source} → {target}".replace('"', "&quot;")
            lines.append(f'  {endpoint(source)} -->|"{label}"| {endpoint(target)}')
        return current

    expand(root, [])
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("example", type=Path, help="Folder containing main.json and components/")
    parser.add_argument("--markdown", action="store_true", help="Wrap output in a Mermaid Markdown code fence")
    args = parser.parse_args()
    try:
        diagram = mermaid(*load_example(args.example))
    except (OSError, ValueError, KeyError, json.JSONDecodeError) as exc:
        parser.exit(1, f"error: {exc}\n")
    sys.stdout.write("```mermaid\n" + diagram + "```\n" if args.markdown else diagram)


if __name__ == "__main__":
    main()
