from src.downloader import downloader

class TestDownloader:
    def test_process(self):
        res = downloader.process()
        assert res == True
