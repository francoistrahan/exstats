from unittest.mock import patch

from pytest import fixture, raises

from exstats.app import run



class ExitException(Exception):
    def __init__(self, code, message) -> None:
        self.message = message
        self.code = code



@fixture
def exitmock():
    def raiseOnExit(self, code=0, message=None):
        raise ExitException(code, message)


    with patch("argparse.ArgumentParser.exit", raiseOnExit) as patcher:
        yield patcher



def test_noparams(exitmock, capsys):
    EXPECTED_ERR = "usage: exstat [-h] SRC [SRC ...]\n"
    EXPECTED_OUT = ""

    with raises(ExitException) as ex:
        run([])

        assert ex.value.code == 0

    out, err = capsys.readouterr()

    assert EXPECTED_OUT == out
    assert EXPECTED_ERR == err



def test_help(exitmock, capsys):
    EXPECTED_ERR = ""
    EXPECTED_OUT = ("usage: exstat [-h] SRC [SRC ...]\n"
                    "\n"
                    "Computes disk usage statistics by file extension\n"
                    "\n"
                    "positional arguments:\n"
                    "  SRC         A file or a folder to be included\n"
                    "\n"
                    "optional arguments:\n"
                    "  -h, --help  show this help message and exit\n")

    with raises(ExitException) as ex:
        run("-h".split())

        assert ex.value.code == 0

    out, err = capsys.readouterr()

    assert EXPECTED_OUT == out
    assert EXPECTED_ERR == err
