from __future__ import print_function
from tqdm import tqdm
import base64
import datetime
import distutils.core
import os
import random
import re
import requests
import string
import subprocess as sp
import urllib.parse as urlparse
from src.settings import VIDEO_PATH
from src.file_service import file_service

TIMESTAMP = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
SALT = ''.join(random.choice(string.digits) for _ in range(3))
OUT_PREFIX = TIMESTAMP + '-' + SALT
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
TEMP_DIR = os.path.join(BASE_DIR, "temp")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")


class Vimeo:
    def is_type(self, url, flag=None):
        if flag == 'vimeo':
            return True

        urls = [
            'adaptive.akamaized.net',
            'skyfire.vimeocdn.com',
        ]

        for item in urls:
            if item in url:
                return True

    def download(self, url, dir='other', name=OUT_PREFIX):
        path = VIDEO_PATH + dir + '/'
        file_service.create_dir(path)

        temp_dir = os.path.join(path, 'temp', OUT_PREFIX)
        file_service.create_dir(temp_dir)

        filename_path = os.path.join(path, '{}_video.mp4'.format(name))

        resp = requests.get(url)
        if resp.status_code != 200:
            match = re.search(r'<TITLE>(.+)<\/TITLE>', str(resp.content))
            title = match.group(1) if match else str(resp.content)
            print('HTTP error (' + str(resp.status_code) + '): ' + title)
            raise Exception("Vimeo something wrong")

        content = resp.json()
        base_url = urlparse.urljoin(url, content['base_url'])

        self._download_video(base_url, content['video'], temp_dir)
        self._download_audio(base_url, content['audio'], temp_dir)
        self._merge_audio_video(filename_path, temp_dir)

    def _download_video(self, base_url, content, temp_dir):
        heights = [(i, d['height']) for (i, d) in enumerate(content)]
        idx, _ = min(heights, key=lambda t: t[1])
        video = content[idx]
        video_base_url = urlparse.urljoin(base_url, video['base_url'])
        filename = os.path.join(temp_dir, "v.mp4")

        video_file = open(filename, 'wb')
        init_segment = base64.b64decode(video['init_segment'])
        video_file.write(init_segment)

        for segment in tqdm(video['segments']):
            segment_url = video_base_url + segment['url']
            resp = requests.get(segment_url, stream=True)

            if resp.status_code != 200:
                print('not 200!', resp, segment_url)
                raise Exception("Vimeo something wrong")
                break

            for chunk in resp:
                video_file.write(chunk)

        video_file.flush()
        video_file.close()

    def _download_audio(self, base_url, content, temp_dir):
        audio = content[0]
        audio_base_url = urlparse.urljoin(base_url, audio['base_url'])
        filename = os.path.join(temp_dir, "a.mp3")

        audio_file = open(filename, 'wb')
        init_segment = base64.b64decode(audio['init_segment'])
        audio_file.write(init_segment)

        for segment in tqdm(audio['segments']):
            segment_url = audio_base_url + segment['url']
            resp = requests.get(segment_url, stream=True)

            if resp.status_code != 200:
                print('not 200!', segment_url, resp)
                raise Exception("Vimeo something wrong")
                break

            for chunk in resp:
                audio_file.write(chunk)

        audio_file.flush()
        audio_file.close()

    def _merge_audio_video(self, filename_path, temp_dir):
        video_filename = os.path.join(temp_dir, "v.mp4")
        audio_filename = os.path.join(temp_dir, "a.mp3")

        FFMPEG_BIN = distutils.spawn.find_executable("ffmpeg")

        command = [
            FFMPEG_BIN, '-i', audio_filename, '-i', video_filename, '-acodec',
            'copy', '-vcodec', 'copy', filename_path
        ]

        print("ffmpeg command is:", command)
        sp.call(command)


vimeo = Vimeo()
