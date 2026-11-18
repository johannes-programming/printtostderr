__all__: list[str] = ["main", "parse_args", "printtostderr", "run"]

import argparse
import logging
import sys
from collections import abc
from importlib import metadata
from typing import Any


def main(args: abc.Iterable[object] | None = None) -> int:
    "This function parses the args and hands them to the printtostderr function."
    space: argparse.Namespace
    try:
        space = parse_args(args)
        run(*space.args)
    except SystemExit as exit:
        if isinstance(exit.code, int):
            return int(exit.code)
        else:
            return int(bool(exit.code))
    except BaseException as exc:
        logging.exception(exc)
        return 1
    else:
        return 0


def parse_args(args: abc.Iterable[object] | None = None) -> argparse.Namespace:
    parser: argparse.ArgumentParser
    version: str
    parser = argparse.ArgumentParser(
        add_help=False,
        description="Print to stderr.",
        fromfile_prefix_chars="@",
        prog="printtostderr",
    )
    version = "%(prog)s, version " + metadata.version("printtostderr")
    parser.add_argument(
        "--end",
        default="\n",
        help="end the printout",
    )
    parser.add_argument(
        "--sep",
        default=" ",
        help="separate between the args",
    )
    parser.add_argument(
        "-V",
        "--version",
        action="version",
        help="print version and abort",
        version=version,
    )
    parser.add_argument(
        "-h",
        "--help",
        action="help",
        help="print this message and abort",
    )
    parser.add_argument(
        "args",
        help="print args to stderr",
        nargs="*",
    )
    if args is None:
        return parser.parse_args()
    else:
        return parser.parse_args(map(str, args))


def printtostderr(*args: object, **kwargs: Any) -> None:
    "This function prints to sys.stderr."
    print(*args, **kwargs, file=sys.stderr)


def run(*args: object, end: str = "\n", sep: str = " ") -> None:
    printtostderr(*args, end=end, sep=sep)
