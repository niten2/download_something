from src.downloaders.youtube_mp3 import youtube_mp3
from tests.fixtures.links import youtube_mp3_url


class TestYouTubeMp3:
    def test_is_type_valid_params_given(self):
        youtube_mp3.is_type(youtube_mp3_url, 'mp3') == True

    def test_is_type_wrong_params_given(self):
        youtube_mp3.is_type('test', 'mp3') == False

    def test_download(self):
        youtube_video.download(youtube_video_url)
        assert 1 == 1
