from pytube import YouTube
from src.utils import utils
from src.settings import VIDEO_PATH
from src.file_service import file_service

class YoutubeVideo:
	def is_type(self, url):
		return "youtube" in url

	@utils.spinner
	def download(self, url, dir='other'):
		full_path = VIDEO_PATH + dir
		file_service.create_dir(full_path)

		try:
			YouTube(url).streams.first().download(full_path)
		except Exception as e:
			print(e)

youtube_video = YoutubeVideo()
