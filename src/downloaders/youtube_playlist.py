from pytube import Playlist
from src.utils import spinner

# TODO
class YoutubePlaylist:
	def isType(self, url):
		return "youtube" in url and "list" in url

	def process(link):
		videos = self.__get_links(link)

		for video in videos:
			fileService.append_link(video + ',' + dir_name)

	@spinner
	def _get_links(self, url, dir):
		pl = Playlist(url, True)
		links = pl.parse_links()
		array = []

		for link in links:
			array.append(['https://www.youtube.com/' + link, dir])

		return array

		# full_path = PATH + dir
		# files.create_dir(full_path)

Youtube_playlist = YoutubePlaylist()
