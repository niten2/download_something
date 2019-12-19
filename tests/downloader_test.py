from src.downloader import downloader

class TestDownloader:
    def test_process(self):
        downloader.process()
        assert 1 == 1
