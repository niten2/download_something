from __future__ import unicode_literals
import youtube_dl
from src.utils import utils
from src.settings import VIDEO_PATH
from src.file_service import file_service

class YoutubeVideo:
    def is_type(self, url):
        return "youtube" in url

    def download(self, url, dir='other'):
        full_path = VIDEO_PATH + dir + '/'
        file_service.create_dir(full_path)
        ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',
            'outtmpl': full_path + '/%(title)s.%(ext)s',
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

youtube_video = YoutubeVideo()
