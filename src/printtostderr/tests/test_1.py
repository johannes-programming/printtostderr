import io
import unittest
from contextlib import redirect_stderr
from typing import *

from printtostderr.core import main, printtostderr

__all__ = ["TestMainAndPrintToStderr"]


class TestMainAndPrintToStderr(unittest.TestCase):

    def test_printtostderr(self: Self) -> None:
        "This test tests if printtostderr prints correctly to sys.stderr."
        output: Any
        stderr: io.StringIO
        stderr = io.StringIO()
        with redirect_stderr(stderr):
            printtostderr("This is a test", 123, "!", sep="-", end="\n")
        output = stderr.getvalue()
        self.assertEqual(output, "This is a test-123-!\n")

    def test_main_with_args(self: Self) -> None:
        "This test tests main with specific arguments."
        output: Any
        stderr: io.StringIO
        stderr = io.StringIO()
        with redirect_stderr(stderr):
            main(["arg1", "arg2", "arg3"])
        output = stderr.getvalue()
        self.assertEqual(output, "arg1 arg2 arg3\n")

    def test_main_without_args(self: Self) -> None:
        "This test tests main with no arguments."
        output: Any
        stderr: io.StringIO
        stderr = io.StringIO()
        with redirect_stderr(stderr):
            main()
        output = stderr.getvalue()
        self.assertEqual(output, "\n")


if __name__ == "__main__":
    unittest.main()
