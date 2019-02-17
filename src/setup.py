#! /usr/bin/env python3

from os import umask
from libexstats import __version__

from distutils.core import setup

umask(0o022)

setup(
    name='extstats',
    version=__version__,
    description='Scipts to computes disk usage satistics by file extension',
    author='François Trahan',
    author_email='francois.trahan@gmail.com',
    url='https://rm.ftrahan.com/projects/exstats',
    packages=[
        "libexstats",
        ],
    scripts=[
        "exstats",
        ],
#    data_files=[
#        (
#            "share/libftbackup/samples",
#            [
#                "samples/exclude.regex",
#                "samples/nocompress.regex",
#                "samples/prune.regex",
#                "samples/wraperscript",
#                ]),
#        ],
    )
