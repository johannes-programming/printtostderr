import argparse
import sys
from typing import *

__all__ = ["main", "printtostderr"]


def main(args: Optional[Iterable] = None) -> None:
    "This function parses the args and hands them to the printtostderr function."
    args_: Iterable
    parser: argparse.ArgumentParser
    space: argparse.Namespace
    if args is None:
        args_ = args
    else:
        args_ = list(map(str, args))
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "args", nargs="*", help="These arguments will be printed to sys.stderr."
    )
    space = parser.parse_args(args_)
    printtostderr(*space.args)


def printtostderr(*args: Any, **kwargs: Any) -> None:
    "This function prints to sys.stderr."
    print(*args, **kwargs, file=sys.stderr)
