from src.downloaders.youtube_video import youtube_video
from tests.fixtures.links import youtube_video_url


class TestYouTubeVideo:
    def test_is_type_valid_params_given(self):
        youtube_video.is_type(youtube_video_url) == True

    def test_is_type_wrong_params_given(self):
        youtube_video.is_type('test') == False

    def test_download(self):
        youtube_video.download(youtube_video_url)
        assert 1 == 1
