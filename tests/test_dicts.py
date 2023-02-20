from utils import dicts
import pytest

@pytest.fixture
def coll():
    return {"vcs": "mercurial", "ide": "pycharm", "framework": "django"}


def test_get(coll):
    assert dicts.get_val(coll, "dot", 'git') == 'git'


def test_get2(coll):
    assert dicts.get_val(coll, "vcs", 'git') == 'mercurial'
    assert dicts.get_val(coll, "ide", 'git') == 'pycharm'


def teat_get3():
    assert dicts.get_val({}, "vcs", 'git') == "git"
    assert dicts.get_val({}, "vcs", 'another') == "another"

