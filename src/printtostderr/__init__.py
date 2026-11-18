__all__: list[str] = ["main", "parse_args", "printtostderr", "run", "test"]

import sys

from printtostderr.core import main, parse_args, printtostderr, run
from printtostderr.tests import test

if __name__ == "__main__":
    sys.exit(main())
