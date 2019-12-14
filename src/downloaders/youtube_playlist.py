from pytube import Playlist
from src.utils import utils
from src.file_service import file_service

class YoutubePlaylist:
    def is_type(self, url, flag):
        return "youtube" in url and "list" in url in flag == "list"

    def process(self, link, dir):
        res = self._get_links(link, dir)
        file_service.remove_link(link)
        file_service.append_lines(res)

    @utils.spinner
    def _get_links(self, url, dir):
        pl = Playlist(url, True)
        links = pl.parse_links()
        array = []

        for link in links:
            url = ('https://www.youtube.com/' + link + ", " + dir)
            array.append(url)

        return "\n".join(array)

youtube_playlist = YoutubePlaylist()
