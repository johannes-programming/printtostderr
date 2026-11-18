__all__: list[str] = ["TestMain"]

import io
import unittest
from contextlib import redirect_stderr, redirect_stdout
from typing import Self
from unittest.mock import MagicMock, patch

from printtostderr.core import main


class TestMain(unittest.TestCase):

    def test_success_exit_code(self: Self, /) -> None:
        "This test tests the successful exit code."
        status: int
        stderr: io.StringIO
        stderr = io.StringIO()
        with redirect_stderr(stderr):
            status = main(["first", "second"])
        self.assertEqual(status, 0)
        self.assertEqual(stderr.getvalue(), "first second\n")

    def test_object_args(self: Self, /) -> None:
        "This test tests main with non-string arguments."
        status: int
        stderr: io.StringIO
        stderr = io.StringIO()
        with redirect_stderr(stderr):
            status = main(["value", 123])
        self.assertEqual(status, 0)
        self.assertEqual(stderr.getvalue(), "value 123\n")

    def test_help_exit_code(self: Self, /) -> None:
        "This test tests the help exit code."
        status: int
        stdout: io.StringIO
        stdout = io.StringIO()
        with redirect_stdout(stdout):
            status = main(["--help"])
        self.assertEqual(status, 0)
        self.assertIn("usage: printtostderr", stdout.getvalue())

    def test_version_exit_code(self: Self, /) -> None:
        "This test tests the version exit code."
        status: int
        stdout: io.StringIO
        stdout = io.StringIO()
        with patch(
            "printtostderr.core.metadata.version", return_value="1.2.0+local"
        ):
            with redirect_stdout(stdout):
                status = main(["-V"])
        self.assertEqual(status, 0)
        self.assertEqual(
            stdout.getvalue(), "printtostderr, version 1.2.0+local\n"
        )

    def test_invalid_option_exit_code(self: Self, /) -> None:
        "This test tests the argument error exit code."
        status: int
        stderr: io.StringIO
        stderr = io.StringIO()
        with redirect_stderr(stderr):
            status = main(["--unknown"])
        self.assertEqual(status, 2)
        self.assertIn("unrecognized arguments", stderr.getvalue())

    def test_unexpected_error_exit_code(self: Self, /) -> None:
        "This test tests the exit code for an unexpected error."
        log_exception: MagicMock
        status: int
        with patch(
            "printtostderr.core.run", side_effect=RuntimeError("failed")
        ):
            with patch(
                "printtostderr.core.logging.exception"
            ) as log_exception:
                status = main(["first"])
        self.assertEqual(status, 1)
        log_exception.assert_called_once()

    def test_system_exit_code(self: Self, /) -> None:
        "This test tests preserving a SystemExit code."
        status: int
        with patch("printtostderr.core.run", side_effect=SystemExit(3)):
            status = main(["first"])
        self.assertEqual(status, 3)

    def test_system_exit_message(self: Self, /) -> None:
        "This test tests converting a SystemExit message to an error code."
        status: int
        with patch("printtostderr.core.run", side_effect=SystemExit("failed")):
            status = main(["first"])
        self.assertEqual(status, 1)

    def test_main_uses_run(self: Self, /) -> None:
        "This test tests that main passes the arguments to run."
        mocked_run: MagicMock
        status: int
        with patch("printtostderr.core.run") as mocked_run:
            status = main(["first", "second"])
        self.assertEqual(status, 0)
        mocked_run.assert_called_once_with("first", "second")


if __name__ == "__main__":
    unittest.main()
