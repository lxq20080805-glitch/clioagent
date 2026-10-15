"""ClioAgent command-line interface backed by the bundled GraphRAG engine."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


def _project_root(value: str) -> Path:
    root = Path(value).expanduser().resolve()
    if not (root / "settings.yaml").is_file():
        raise SystemExit(f"No ClioAgent settings.yaml found in {root}")
    return root


def _run_graphrag(arguments: list[str]) -> int:
    return subprocess.run(
        [sys.executable, "-m", "graphrag", *arguments], check=False
    ).returncode


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="clioagent",
        description="Index and query historical evidence and historiography.",
    )
    parser.add_argument(
        "--root",
        default=".",
        help="ClioAgent repository directory (default: current directory)",
    )
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("index", help="Build the history knowledge graph")
    commands.add_parser("update", help="Update an existing index")

    query = commands.add_parser("query", help="Ask a question about the corpus")
    query.add_argument("question")
    query.add_argument(
        "--method",
        choices=("local", "global", "drift", "basic"),
        default="local",
        help="Retrieval method (default: local)",
    )
    query.add_argument(
        "--response-type",
        default="IB History evidence and historiography analysis",
    )
    return parser


def main() -> int:
    """Run ClioAgent."""
    args = _build_parser().parse_args()
    root = _project_root(args.root)

    if args.command in {"index", "update"}:
        return _run_graphrag(
            [args.command, "--root", str(root), "--method", "standard"]
        )

    return _run_graphrag(
        [
            "query",
            args.question,
            "--root",
            str(root),
            "--method",
            args.method,
            "--response-type",
            args.response_type,
        ]
    )


if __name__ == "__main__":
    raise SystemExit(main())

