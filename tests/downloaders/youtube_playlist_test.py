from src.downloaders.youtube_playlist import youtube_playlist
from tests.fixtures.links import youtube_playlist_url

class TestYouTubeVideo:
    def test_is_type_valid_params_given(self):
        youtube_playlist.is_type(youtube_playlist_url) == True

    def test_is_type_wrong_params_given(self):
        youtube_playlist.is_type('test') == False

    # def test_process(self):
    #     youtube_playlist.process(youtube_playlist_url, 'dirname')
    #     assert 1 == 1
