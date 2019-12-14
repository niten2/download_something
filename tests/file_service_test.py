from src.file_service import file_service


class TestFileService:
	def test_remove_link(self):
		file_service.remove_link('tttttt')
		assert 1 == 1
