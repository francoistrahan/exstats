from setuptools import find_packages, setup

from exstats import VERSION



setup(
    name='extstats',
    version=VERSION,
    description='Scipts to computes disk usage satistics by file extension',
    url='https://rm.ftrahan.com/projects/exstats',

    author='François Trahan',
    author_email='francois.trahan@gmail.com',

    packages=find_packages(),

    entry_points={
        'console_scripts': [
            'extstats = extstats.__main__:main',
            ],
        },

    )
