import os
import re
from src.settings import LINKS_PATH

class FileService:
    def create_dir(self, path):
        if not os.path.exists(path):
            os.makedirs(path)

    def get_link(self):
        lines = self._get_lines(self._read_file())

        return lines[0]

    def append_lines(self, lines=''):
        res = self._read_file()
        res = res + "\n" + lines

        self._save_file(res)

    def remove_link(self, url):
        lines = self._get_lines(self._read_file())
        lines = list(filter(lambda x: x['url'] != url, lines))
        lines = list(map(lambda x: list(x.values()), lines))
        lines = list(map(lambda x: ", ".join(x), lines))
        lines = "\n".join(lines)

        self._save_file(lines)

    def _read_file(self):
        file = open(LINKS_PATH, 'r')
        lines = file.read()
        file.close()

        return lines or []

    def _save_file(self, res):
        with open(LINKS_PATH, 'w') as f:
            f.write(res)

    def _get_lines(self, lines=''):
        def split(link):
            res = link.split(',')
            url = res[0].strip()
            dir = res[1].strip() if 1 < len(res) else 'other'
            flag = res[2].strip() if 2 < len(res) else ''

            return dict(url=url, dir=dir, flag=flag)

        lines = lines.split('\n')
        lines = list(filter(lambda x: x != '', lines))
        lines = list(filter(lambda x: x.find("TODO") == -1, lines))
        lines = list(map(lambda x: split(x), lines))

        return lines

file_service = FileService()
