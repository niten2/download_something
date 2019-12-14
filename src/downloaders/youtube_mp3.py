import youtube_dl

class YoutubeMp3:
	def is_type(url, flag):
		return 'youtube' in url and flag == 'mp3'

	def get_path(dir_name):
		return MP3_PATH + dir_name

	def download(url, dir_name):
		# TODO add path
		ydl_opts = {
			'format': 'bestaudio/best',
			'postprocessors': [{
				'key': 'FFmpegExtractAudio',
				'preferredcodec': 'mp3',
				'preferredquality': '192',
			}],
		}
		with youtube_dl.YoutubeDL(ydl_opts) as ydl:
			ydl.download(links)

youtube_mp3 = YoutubeMp3()
