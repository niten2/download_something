# import youtube_dl
from src.settings import MP3_PATH

class YoutubeMp3:
	def is_type(self, url, flag):
		return 'youtube' in url and flag == 'mp3'

	def download(self, url, dir_name):
		return None

		# MP3_PATH
		# ydl_opts = {
		# 	'format': 'bestaudio/best',
		# 	'postprocessors': [{
		# 		'key': 'FFmpegExtractAudio',
		# 		'preferredcodec': 'mp3',
		# 		'preferredquality': '192',
		# 	}],
		# }
		# with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		# 	ydl.download(links)

youtube_mp3 = YoutubeMp3()
