from src.utils import utils

class TestFileService:
	def test_remove_link_1(self):
		url = 'test'
		res = utils.is_downloadable(url)
		assert res == False

	def test_remove_link_2(self):
		url = 'https://github.com/niten2/test_tasks'
		res = utils.is_downloadable(url)
		assert res == True
