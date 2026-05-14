import argparse
import sys
from collections.abc import Iterable
from typing import Any, Optional

__all__ = ["main", "printtostderr"]


def main(args: Optional[Iterable[str]] = None) -> None:
    "This function parses the args and hands them to the printtostderr function."
    parser: argparse.ArgumentParser
    space: argparse.Namespace
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "args",
        nargs="*",
        help="These arguments will be printed to sys.stderr.",
    )
    space = parser.parse_args(args)
    printtostderr(*space.args)


def printtostderr(*args: object, **kwargs: Any) -> None:
    "This function prints to sys.stderr."
    print(*args, **kwargs, file=sys.stderr)
