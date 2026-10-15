from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase

from clioagent.cli import _build_parser, _project_root


class CliTests(TestCase):
    def test_query_defaults_to_local(self) -> None:
        args = _build_parser().parse_args(["query", "Why did the regime fall?"])
        self.assertEqual(args.method, "local")

    def test_project_root_accepts_settings(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "settings.yaml").write_text("input: {}\n", encoding="utf-8")
            self.assertEqual(_project_root(str(root)), root.resolve())

