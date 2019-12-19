from src.downloaders.youtube_playlist import youtube_playlist
from tests.fixtures.links import youtube_playlist_url_1, youtube_playlist_url_2
from src.settings import PLAYLIST_FLAG

class TestYouTubeVideo:
    def test_is_type_valid_params_given(self):
        youtube_playlist.is_type(youtube_playlist_url_1, PLAYLIST_FLAG) == True
        youtube_playlist.is_type(youtube_playlist_url_2, PLAYLIST_FLAG) == True

    def test_is_type_wrong_params_given(self):
        youtube_playlist.is_type('test', PLAYLIST_FLAG) == False
        youtube_playlist.is_type('test') == False

    def test_process(self):
        res = youtube_playlist.process(youtube_playlist_url_1)
        assert len(res) > 1
