from src.file_service import file_service
from src.logger import logger
from src.downloaders.git import git
from src.downloaders.wget import wget
from src.downloaders.youtube_mp3 import youtube_mp3
from src.downloaders.youtube_video import youtube_video
from src.downloaders.youtube_playlist import youtube_playlist

errors = [
    "Name or service not known",
    "Too Many Requests",
    "url_encoded_fmt_stream_map",
    "Temporary failure in name resolution",
    "Connection reset by peer",
]


def get_log_string(url, dir=' ', flag=' ', prefix=''):
    return (url + ', ' + dir + ', ' + flag + ', ' + prefix)


class Downloader:
    def process(self):
        link = file_service.get_link()

        if not link:
            return False

        url = link['url']
        dir = link['dir']
        flag = link['flag']

        print('processing', url, dir, flag)

        try:
            raise Exception("Name or service not known")

            if youtube_playlist.is_type(url, flag):
                logger.info('ACTION youtube_playlist ' + url)
                urls = youtube_playlist.process(url, dir)
                if len(urls):
                    file_service.append_lines(urls)
            elif git.is_type(url):
                logger.info('ACTION git ' + url)
                git.download(url)
            elif youtube_mp3.is_type(url, flag):
                logger.info('ACTION youtube video mp3 ' + url)
                youtube_mp3.download(url, dir)
            elif youtube_video.is_type(url):
                logger.info('ACTION youtube video ' + url)
                youtube_video.download(url, dir)
            else:
                logger.info('ACTION wget download ' + url)
                wget.download(url)

            logger.warning(get_log_string('DOWNLOAD LINK:', url, dir, flag))
            file_service.remove_link(url)
        except Exception as err:
            for name in errors:
                if name in str(err):
                    logger.warning(get_log_string(url, dir, flag, str(err)))
                    return False

            logger.warning(
                get_log_string(url, dir, flag, 'REMOVE LINK ' + str(err)))

            file_service.remove_link(url)

        return True


downloader = Downloader()
