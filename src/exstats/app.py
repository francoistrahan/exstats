#! /usr/bin/python3

from argparse import ArgumentParser

from . import getData



NO_EXTENSION = "---"



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

    data = getData(givenPaths)
    data = sorted(data.items(), key=lambda d: d[1])
    for ext, size in data:
        print("{} : {}".format(ext or NO_EXTENSION, size))