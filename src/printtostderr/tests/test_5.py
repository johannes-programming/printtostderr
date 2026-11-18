__all__: list[str] = ["TestPublicImports"]

import unittest
from typing import Self

import printtostderr
from printtostderr import core
from printtostderr.tests import test


class TestPublicImports(unittest.TestCase):

    def test_main(self: Self, /) -> None:
        "This test tests importing main from the package."
        self.assertIs(printtostderr.main, core.main)

    def test_parse_args(self: Self, /) -> None:
        "This test tests importing parse_args from the package."
        self.assertIs(printtostderr.parse_args, core.parse_args)

    def test_printtostderr(self: Self, /) -> None:
        "This test tests importing printtostderr from the package."
        self.assertIs(printtostderr.printtostderr, core.printtostderr)

    def test_run(self: Self, /) -> None:
        "This test tests importing run from the package."
        self.assertIs(printtostderr.run, core.run)

    def test_runner(self: Self, /) -> None:
        "This test tests importing the test runner from the package."
        self.assertIs(printtostderr.test, test)


if __name__ == "__main__":
    unittest.main()
