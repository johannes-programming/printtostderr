import argparse
import sys
from collections import abc
from typing import Any

__all__ = ["main", "printtostderr"]


def main(args: abc.Iterable[object] | None = None) -> None:
    "This function parses the args and hands them to the printtostderr function."
    args_: abc.Iterable[str] | None
    parser: argparse.ArgumentParser
    space: argparse.Namespace
    if args is None:
        args_ = args
    else:
        args_ = list(map(str, args))
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "args",
        nargs="*",
        help="These arguments will be printed to sys.stderr.",
    )
    space = parser.parse_args(args_)
    printtostderr(*space.args)


def printtostderr(*args: object, **kwargs: Any) -> None:
    "This function prints to sys.stderr."
    print(*args, **kwargs, file=sys.stderr)
