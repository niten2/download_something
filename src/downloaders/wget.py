import os
from src.settings import FILES_PATH
from src.file_service import file_service


class Wget:
    def download(self, url):
        file_service.create_dir(FILES_PATH)
        filename = url.split("/")[-1]
        command = "wget " + url + " -O " + FILES_PATH + filename
        os.system(command)


wget = Wget()
