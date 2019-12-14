import os
from dotenv import load_dotenv

load_dotenv(verbose=True)

FILES_PATH = os.getenv("files_path")
GIT_PATH = os.getenv("git_path")
MP3_PATH = os.getenv("mp3_path")
VIDEO_PATH = os.getenv("video_path")

LINKS_PATH = os.getenv("links_path")
LOG_PATH = os.getenv("log_path")
