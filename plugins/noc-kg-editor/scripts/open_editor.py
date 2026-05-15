from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


PLUGIN_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = PLUGIN_ROOT.parents[1]
SRC_ROOT = REPO_ROOT / "src"

if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from notary_kg.editor import build_editor_view  # noqa: E402


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="noc-kg-editor",
        description="Open a safe notary-facing editor view for one usecase KG.",
    )
    parser.add_argument("slug", help="Usecase slug, for example adoption-familienrechtliche-erklaerungen.")
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=REPO_ROOT,
        help="Path to the repository root.",
    )
    parser.add_argument(
        "--format",
        choices=["text", "json", "markdown"],
        default="text",
        help="Output format for the editor view.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Optional output path. Useful with --format markdown for usecase session sheets.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    repo_root = args.repo_root.resolve()

    try:
        view = build_editor_view(repo_root, args.slug)
    except KeyError:
        print(f"ERROR: Unknown KG case slug: {args.slug}", file=sys.stderr)
        return 1

    rendered = render_view(view, args.format)
    if args.output:
        output_path = args.output if args.output.is_absolute() else repo_root / args.output
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(rendered, encoding="utf-8")
        print(f"Wrote KG editor {args.format} view: {output_path}")
        return 0

    print(rendered)
    return 0


def render_view(view: dict[str, Any], output_format: str) -> str:
    if output_format == "json":
        return json.dumps(view, indent=2, ensure_ascii=False)
    if output_format == "markdown":
        return _render_markdown(view)
    return _render_text(view)


def _render_text(view: dict[str, Any]) -> str:
    lines = [
        f"KG editor: {view['title']}",
        f"- slug: {view['usecase_slug']}",
        f"- graph: {view['graph_id']}",
        f"- path: {view['usecase_path']}",
        "",
        "Tabs",
    ]
    for tab in view["editor_model"]["tabs"]:
        lines.append(f"- {tab['label_de']}: {tab['item_count']} items ({tab['render_as']})")
    lines.extend(
        [
            "",
            "Patch boundary",
            f"- mode: {view['patch_policy']['mode']}",
            f"- forbidden fields: {', '.join(view['patch_policy']['forbidden_fields'])}",
            f"- confirmation required: {view['patch_policy']['confirmation_required']}",
            "",
            "Next operator step",
            "- Review open information and request a patch proposal instead of editing raw JSON.",
        ]
    )
    return "\n".join(lines)


def _render_markdown(view: dict[str, Any]) -> str:
    lines = [
        f"# KG Editor Session: {view['title']}",
        "",
        f"- Usecase: `{view['usecase_slug']}`",
        f"- Graph: `{view['graph_id']}`",
        f"- Path: [{view['usecase_path']}/](../../{view['usecase_path']})",
        f"- Patch mode: `{view['patch_policy']['mode']}`",
        "",
        "## Patch Boundary",
        "",
        "- Do not enter real mandate, personal, family, health, estate, property or secret values.",
        "- Do not edit `value` fields.",
        "- Request a patch proposal, validation, diff review and pull request.",
        "",
    ]

    for tab in view["editor_model"]["tabs"]:
        lines.extend(_render_markdown_tab(tab))

    lines.extend(
        [
            "## Actions",
            "",
            *[f"- `{action['name']}`" for action in view["actions"]],
            "",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def _render_markdown_tab(tab: dict[str, Any]) -> list[str]:
    lines = [
        f"## {tab['label_de']}",
        "",
        f"- View type: `{tab['render_as']}`",
        f"- Items: `{tab['item_count']}`",
        "",
    ]
    if "groups" in tab:
        for group in tab["groups"]:
            lines.extend(
                [
                    f"### {group['label_de']}",
                    "",
                    "| Status | ID | Label | Owner |",
                    "| --- | --- | --- | --- |",
                ]
            )
            for item in group["items"]:
                lines.append(
                    f"| `{item.get('status', '')}` | `{item.get('id', '')}` | "
                    f"{item.get('label', '')} | `{item.get('owner_role', '')}` |"
                )
            lines.append("")
        return lines

    lines.extend(["| Status | ID | Label | Frage/Quelle |", "| --- | --- | --- | --- |"])
    for item in tab.get("items", []):
        detail = item.get("question", item.get("source", ""))
        lines.append(
            f"| `{item.get('status', '')}` | `{item.get('id', '')}` | "
            f"{item.get('label', '')} | {detail} |"
        )
    lines.append("")
    return lines


if __name__ == "__main__":
    raise SystemExit(main())

