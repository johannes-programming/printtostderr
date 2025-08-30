import argparse
import sys
from typing import *

__all__ = ["main", "printtostderr"]


def main(args: Optional[Iterable] = None) -> None:
    "This function parses the args and hands them to the printtostderr function."
    values:Optional[list]
    if args is None:
        values = None
    else:
        values = list(map(str, args))
    parser :argparse.ArgumentParser= argparse.ArgumentParser()
    parser.add_argument(
        "args", nargs="*", help="These arguments will be printed to sys.stderr."
    )
    ns :argparse.Namespace= parser.parse_args(values)
    printtostderr(*ns.args)


def printtostderr(*args: Any, **kwargs: Any) -> None:
    "This function prints to sys.stderr."
    print(*args, **kwargs, file=sys.stderr)
