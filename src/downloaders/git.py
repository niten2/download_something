import os
from src.settings import GIT_PATH
from src.file_service import file_service

class Git:
	def is_type(self, url):
		return "git" in url

	def download(self, url):
		file_service.create_dir(GIT_PATH)
		dir = url.split("/")[-1]
		command = "git clone " + url + "/" + " " + GIT_PATH + "/" + dir
		os.system(command)

git = Git()
