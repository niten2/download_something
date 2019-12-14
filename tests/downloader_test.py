from src.downloader import Downloader

downloader = Downloader()

class TestClass:
    def test_run(self):
        links = [
			''
		]

		downloader.run(links)

        assert True == True
