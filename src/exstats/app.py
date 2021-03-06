from argparse import ArgumentParser

import numpy as  np
import pandas as pd

from . import getData



SIZE_FORMATTER = "{:,d}".format



def parseArgs(args):
    from os.path import isfile, isdir, islink

    prs = ArgumentParser(
        prog="exstat",
        description="Computes disk usage statistics by file extension",
        argument_default=None,
        add_help=True,
    )

    prs.add_argument(
        "src",
        nargs="+",
        metavar="SRC",
        help="A file or a folder to be included",
        )

    opts = prs.parse_args(args)

    for p in opts.src:
        if islink(p) or not (isdir(p) or isfile(p)):
            raise Exception('''"{}" is not a valid filename'''.format(p))

    return opts



def run(args):
    opts = parseArgs(args)
    givenPaths = opts.src

    data = getData(givenPaths)

    data.sort_values("Size", inplace=True)

    total = data.Size.sum()

    data["Percentage"] = data.Size / total
    data.Size = data.Size.astype(np.int)

    output = data.to_string(
        formatters={
            "Size": SIZE_FORMATTER,
            "Percentage": "{:.2%}".format,
            },
        max_cols=None,
        max_rows=None,
        )

    print(output)
    print()
    print("Total Size: {} bytes".format(SIZE_FORMATTER(total)))
