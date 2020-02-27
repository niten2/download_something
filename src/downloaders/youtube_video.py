from __future__ import unicode_literals
from src.file_service import file_service
from src.settings import VIDEO_PATH
import youtube_dl


class YoutubeVideo:
    def is_type(self, url):
        return "youtube" in url

    def download(self, url, dir='other'):
        full_path = VIDEO_PATH + dir + '/'
        file_service.create_dir(full_path)

        ydl_opts = {
            'format':
            'bestvideo[height<=?720]+bestaudio[ext=m4a]/best[ext=mp4]/best',
            'writesubtitles': 'write-sub=',
            'subtitleslangs': ['ru', 'en'],
            'outtmpl': full_path + '%(title)s.%(ext)s',
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])


youtube_video = YoutubeVideo()
