from pytube import Playlist
from src.utils import utils
from src.file_service import file_service
from src.settings import DEFAULT_DIR

class YoutubePlaylist:
    def is_type(self, url, flag=""):
        return "youtube" in url and "list" in url and flag == "playlist"

    @utils.spinner
    def process(self, url, dir=DEFAULT_DIR):
        pl = Playlist(url, True)
        links = pl.parse_links()
        array = []

        for link in links:
            url = ('https://www.youtube.com' + link + ", " + dir)
            array.append(url)

        return "\n".join(array)

youtube_playlist = YoutubePlaylist()
