from src.downloaders.git import git
from tests.fixtures.links import git_url

class TestGit:
    def test_is_type_valid_params_given(self):
        assert git.is_type(git_url) == True

    def test_is_type_wrong_params_given(self):
        assert git.is_type('test') == False

    def test_download(self):
        git.download(git_url)
        assert 1 == 1
