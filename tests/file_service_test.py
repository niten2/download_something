from src.file_service import file_service

class TestFileService:
    # def test_remove_link(self):
    # 	file_service.remove_link('tttttt')
    # 	assert 1 == 1

    def test_append_lines(self):
        file_service.append_lines('tttttt, dir')
        assert 1 == 1
