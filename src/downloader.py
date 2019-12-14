from src.logger import logger
from src.utils import utils
from src.donwloaders.git import git
from src.donwloaders.wget import wget
from src.donwloaders.youtube_mp3 import youtube_mp3
from src.donwloaders.youtube_video import youtube_video
from src.donwloaders.youtube_playlist import youtube_playlist

class Downloader:
	def run(self, lines):
		for line in lines:
			try:
				self._execute(line[0], line[1], line[2])
			except Exception as e:
				logger.warning(line[0], str(e))

	def _execute(self, url, dir_name, flag):
		# if not utils.is_downloadable(url):
		# 	raise 'error, wrong type' + url

		if youtube_playlist.is_type(url):
			youtube_playlist.process(url)
		elif git.is_type(url):
			git.download(url, dir_name)
		elif youtube_video.is_type(url):
			youtube_video.download(url)
		elif youtube_mp3.is_type(url, flag):
			youtube_mp3.download(url)
		else:
			wget.download(url)

		file_service.remove_link(url)
		logger.warning('log url ' + url)

downloader = Downloader()
