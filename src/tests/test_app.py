from unittest.mock import patch

from pytest import fixture, raises

from exstats.app import run



class ExitException(Exception):
    def __init__(self, code) -> None:
        self.code = code



@fixture
def exitmock():
    def raiseOnExit(code):
        raise ExitException(code)


    with patch("argparse.ArgumentParser.exit", raiseOnExit) as patcher:
        yield patcher



def test_help(exitmock, capsys):
    EXPECTED_ERR = ""
    EXPECTED_OUT = """usage: exstat [-h] SRC [SRC ...]

Computes disk usage statistics by file extension

positional arguments:
  SRC         A file or a folder to be included

optional arguments:
  -h, --help  show this help message and exit
"""

    with raises(ExitException) as ex:
        run("-h".split())

        assert ex.value.code == 0

    out, err = capsys.readouterr()

    assert EXPECTED_OUT == out
    assert EXPECTED_ERR == err
