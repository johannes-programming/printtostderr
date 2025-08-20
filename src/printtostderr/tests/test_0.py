import io
import sys
import unittest
from typing import *

from printtostderr.core import main, printtostderr

__all__ = ["TestMainAndPrintToStderr"]


class TestMainAndPrintToStderr(unittest.TestCase):

    def test_printtostderr(self: Self) -> None:
        "This test tests if printtostderr prints correctly to sys.stderr."
        stderr: io.StringIO
        original_stderr: Any
        output: Any
        stderr = io.StringIO()
        original_stderr = sys.stderr
        try:
            sys.stderr = stderr
            printtostderr("This is a test", 123, "!", sep="-", end="\n")
            output = stderr.getvalue()
        finally:
            sys.stderr = original_stderr
        self.assertEqual(output, "This is a test-123-!\n")

    def test_main_with_args(self: Self) -> None:
        "This test tests main with specific arguments."
        original_stderr: Any
        output: Any
        stderr: io.StringIO
        stderr = io.StringIO()
        original_stderr = sys.stderr
        try:
            sys.stderr = stderr
            main(["arg1", "arg2", "arg3"])
            output = stderr.getvalue()
        finally:
            sys.stderr = original_stderr
        self.assertEqual(output, "arg1 arg2 arg3\n")

    def test_main_without_args(self: Self) -> None:
        "This test tests main with no arguments."
        original_stderr: Any
        output: Any
        stderr: io.StringIO
        stderr = io.StringIO()
        original_stderr = sys.stderr
        try:
            sys.stderr = stderr
            main(args=())
            output = stderr.getvalue()
        finally:
            sys.stderr = original_stderr
        self.assertEqual(output, "\n")


if __name__ == "__main__":
    unittest.main()
