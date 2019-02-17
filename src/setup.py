from setuptools import find_packages, setup

from exstats import VERSION



setup(
    name='exstats',
    version=VERSION,
    description='Scipts to computes disk usage satistics by file extension',
    url='https://rm.ftrahan.com/projects/exstats',

    author='François Trahan',
    author_email='francois.trahan@gmail.com',

    packages=find_packages(),

    entry_points={
        'console_scripts': [
            'exstats = exstats.__main__:main',
            ],
        },

    install_requires=[
        "pandas",
        "numpy",
        ]

    )
