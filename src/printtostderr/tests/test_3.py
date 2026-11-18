__all__: list[str] = ["TestRun"]

import io
import unittest
from contextlib import redirect_stderr
from typing import Self

from printtostderr.core import run


class TestRun(unittest.TestCase):

    def test_default_output(self: Self, /) -> None:
        "This test tests the default output of run."
        stderr: io.StringIO
        stderr = io.StringIO()
        with redirect_stderr(stderr):
            run("first", "second")
        self.assertEqual(stderr.getvalue(), "first second\n")

    def test_custom_end(self: Self, /) -> None:
        "This test tests the end argument of run."
        stderr: io.StringIO
        stderr = io.StringIO()
        with redirect_stderr(stderr):
            run("first", end="!")
        self.assertEqual(stderr.getvalue(), "first!")

    def test_custom_sep(self: Self, /) -> None:
        "This test tests the sep argument of run."
        stderr: io.StringIO
        stderr = io.StringIO()
        with redirect_stderr(stderr):
            run("first", "second", sep=":")
        self.assertEqual(stderr.getvalue(), "first:second\n")

    def test_custom_end_and_sep(self: Self, /) -> None:
        "This test tests both formatting arguments of run."
        stderr: io.StringIO
        stderr = io.StringIO()
        with redirect_stderr(stderr):
            run("first", "second", end="!", sep=":")
        self.assertEqual(stderr.getvalue(), "first:second!")

    def test_objects(self: Self, /) -> None:
        "This test tests run with non-string objects."
        stderr: io.StringIO
        stderr = io.StringIO()
        with redirect_stderr(stderr):
            run("value", 123, None)
        self.assertEqual(stderr.getvalue(), "value 123 None\n")

    def test_without_args(self: Self, /) -> None:
        "This test tests run without positional arguments."
        stderr: io.StringIO
        stderr = io.StringIO()
        with redirect_stderr(stderr):
            run()
        self.assertEqual(stderr.getvalue(), "\n")


if __name__ == "__main__":
    unittest.main()
