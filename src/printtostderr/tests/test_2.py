__all__: list[str] = ["TestParseArgs"]

import argparse
import io
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Any, Self
from unittest.mock import patch

from printtostderr.core import parse_args


class TestParseArgs(unittest.TestCase):

    def test_defaults(self: Self, /) -> None:
        "This test tests the default argument values."
        space: argparse.Namespace
        space = parse_args(())
        self.assertEqual(space.args, [])
        self.assertEqual(space.end, "\n")
        self.assertEqual(space.sep, " ")

    def test_positional_args(self: Self, /) -> None:
        "This test tests positional arguments."
        space: argparse.Namespace
        space = parse_args(["first", "second"])
        self.assertEqual(space.args, ["first", "second"])

    def test_object_args(self: Self, /) -> None:
        "This test tests converting objects to strings."
        space: argparse.Namespace
        space = parse_args(["first", 123, None])
        self.assertEqual(space.args, ["first", "123", "None"])

    def test_end_and_sep(self: Self, /) -> None:
        "This test tests the end and separator options."
        space: argparse.Namespace
        space = parse_args(["--end", "!", "--sep", ":", "first", "second"])
        self.assertEqual(space.args, ["first", "second"])
        self.assertEqual(space.end, "!")
        self.assertEqual(space.sep, ":")

    def test_args_from_file(self: Self, /) -> None:
        "This test tests reading arguments from a file."
        directory: str
        path: Path
        space: argparse.Namespace
        with TemporaryDirectory() as directory:
            path = Path(directory) / "args.txt"
            path.write_text("first\nsecond\n", encoding="utf-8")
            space = parse_args(["@" + str(path)])
        self.assertEqual(space.args, ["first", "second"])

    def test_help(self: Self, /) -> None:
        "This test tests the help option."
        caught: Any
        stdout: io.StringIO
        stdout = io.StringIO()
        with redirect_stdout(stdout):
            with self.assertRaises(SystemExit) as caught:
                parse_args(["--help"])
        self.assertEqual(caught.exception.code, 0)
        self.assertIn("Print to stderr.", stdout.getvalue())
        self.assertIn("--sep", stdout.getvalue())
        self.assertIn("--end", stdout.getvalue())

    def test_version(self: Self, /) -> None:
        "This test tests the version option."
        caught: Any
        stdout: io.StringIO
        stdout = io.StringIO()
        with patch(
            "printtostderr.core.metadata.version", return_value="1.2.0+local"
        ):
            with redirect_stdout(stdout):
                with self.assertRaises(SystemExit) as caught:
                    parse_args(["--version"])
        self.assertEqual(caught.exception.code, 0)
        self.assertEqual(
            stdout.getvalue(), "printtostderr, version 1.2.0+local\n"
        )

    def test_invalid_option(self: Self, /) -> None:
        "This test tests an invalid command-line option."
        caught: Any
        stderr: io.StringIO
        stderr = io.StringIO()
        with redirect_stderr(stderr):
            with self.assertRaises(SystemExit) as caught:
                parse_args(["--unknown"])
        self.assertEqual(caught.exception.code, 2)
        self.assertIn("unrecognized arguments", stderr.getvalue())


if __name__ == "__main__":
    unittest.main()
