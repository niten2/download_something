from __future__ import unicode_literals
import youtube_dl
from src.settings import MP3_PATH

class YoutubeMp3:
    def is_type(self, url, flag):
        return 'youtube' in url and flag == 'mp3'

    def download(self, url, dir):
        full_path = MP3_PATH + dir + '/'
        file_service.create_dir(full_path)

        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': full_path + '%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

youtube_mp3 = YoutubeMp3()
