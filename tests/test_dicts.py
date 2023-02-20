from utils import dicts


def test_get():
    assert dicts.get_val({"vcs": "mercurial"}, "dot", 'git') == 'git'
    assert dicts.get_val({"vcs": "mercurial"}, "vcs", 'git') == 'mercurial'
    assert dicts.get_val({}, "vcs", 'git') == None

