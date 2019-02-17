from argparse import ArgumentParser

import numpy as  np
import pandas as pd

from . import getData



SIZE_FORMATTER = "{:,d}".format



def parseArgs():
    from os.path import isfile, isdir, islink

    prs = ArgumentParser(
        description="Computes disk usage satistics by file extension",
        argument_default=None,
        add_help=True)

    prs.add_argument(
        "src",
        nargs="+",
        metavar="SRC",
        help="A file or a folder to be included",
        )

    opts = prs.parse_args()

    for p in opts.src:
        if islink(p) or not (isdir(p) or isfile(p)):
            raise Exception('''"{}" is not a valid filename'''.format(p))

    return opts



def run():
    opts = parseArgs()
    givenPaths = opts.src

    data: pd.DataFrame = getData(givenPaths)

    data.sort_values("Size", inplace=True)

    total = data.Size.sum()

    data["Percentage"] = data.Size / total
    data.Size = data.Size.astype(np.int)

    output = data.to_string(
        formatters={
            "Size": SIZE_FORMATTER,
            "Percentage": "{:.2%}".format,
            }
        )
    print(output)
    print()
    print("Total Size: {} bytes".format(SIZE_FORMATTER(total)))
