from pytest import fixture, mark, raises

from exstats.app import run



class ExitException(Exception):
    def __init__(self, code, message) -> None:
        self.message = message
        self.code = code



@fixture
def exitmock(monkeypatch):
    def raiseOnExit(self, code=0, message=None):
        raise ExitException(code, message)


    monkeypatch.setattr("argparse.ArgumentParser.exit", raiseOnExit)



@mark.usefixtures("exitmock")
def test_noparams(capsys):
    EXPECTED_ERR = "usage: exstat [-h] SRC [SRC ...]\n"
    EXPECTED_OUT = ""

    with raises(ExitException) as ex:
        run([])

        assert ex.value.code == 0

    out, err = capsys.readouterr()

    assert EXPECTED_OUT == out
    assert EXPECTED_ERR == err



@mark.usefixtures("exitmock")
def test_help(capsys):
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



def test_sampledata(shared_datadir, capsys):
    EXPECTED_OUT = ("          Size Percentage\n"
                    "Extension                \n"
                    "empty        0      0.00%\n"
                    "(none)       7      1.97%\n"
                    "txt        116     32.68%\n"
                    "bin        232     65.35%\n"
                    "\n"
                    "Total Size: 355 bytes\n")

    args = [str(shared_datadir)]
    run(args)
    out, err = capsys.readouterr()

    print(out)
    assert EXPECTED_OUT == out
    assert "" == err
