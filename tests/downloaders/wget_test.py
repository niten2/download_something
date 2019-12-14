from src.downloaders.wget import wget
from tests.fixtures.links import file_url

class TestWget:
    def test_download(self):
        wget.download(file_url)
        assert 1 == 1
