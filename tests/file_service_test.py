from src.file_service import file_service

url = "https://www.youtube.com/playlist?list=PLVFlo87bKU8LBC4vQLo3E6Gghg9U0uALj"

class TestFileService:
    def test_get_link(self):
        res = file_service.get_link()
        assert len(res) > 1

    def test_remove_link(self):
    	file_service.remove_link(url)
    	assert 1 == 1

    def test_append_lines(self):
        line = 'tttttt, dir'
        file_service.append_lines(line)
        assert 1 == 1
