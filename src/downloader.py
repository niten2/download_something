from src.file_service import file_service
from src.logger import logger
from src.downloaders.git import git
from src.downloaders.wget import wget
from src.downloaders.youtube_mp3 import youtube_mp3
from src.downloaders.youtube_video import youtube_video
from src.downloaders.youtube_playlist import youtube_playlist

def get_log_string(prefix, url, dir=' ', flag=' '):
    return prefix + ' ' + url + ', ' + dir + ', ' + flag

class Downloader:
    def process(self):
        link = file_service.get_link()

        if not link:
            return False

        url = link['url']
        dir = link['dir']
        flag = link['flag']

        print('process', url, dir, flag)

        try:
            if youtube_playlist.is_type(url, flag):
                logger.info('ACTION youtube_playlist ' + url)
                urls = youtube_playlist.process(url, dir)
                if len(urls):
                    file_service.append_lines(urls)
            elif git.is_type(url):
                logger.info('ACTION git ' + url)
                git.download(url)
            elif youtube_video.is_type(url):
                logger.info('ACTION youtube video ' + url)
                youtube_video.download(url, dir)
            elif youtube_mp3.is_type(url, flag):
                logger.info('ACTION youtube video mp3 ' + url)
                youtube_mp3.download(url)
            else:
                logger.info('ACTION wget download ' + url)
                wget.download(url)

            logger.warning(get_log_string('DOWNLOAD LINK:', url, dir, flag))
            file_service.remove_link(url)
        except Exception as e:
            logger.warning(get_log_string('REMOVE LINK ' + str(e) + ' :', url, dir, flag))
            file_service.remove_link(url)

        return True

downloader = Downloader()
