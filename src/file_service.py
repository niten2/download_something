import os
import re
from src.settings import LINKS_PATH

class FileService:
    def create_dir(self, path):
        if not os.path.exists(path):
            os.makedirs(path)

    def get_links(self):
        file = open(LINKS_PATH, 'r')
        lines = file.read()
        file.close()

        lines = self._filter_lines(lines)
        return lines

    def append_lines(self, lines):
        res = self._read_file()
        res = res + "\n" + lines
        self._save_file(res)

    def remove_link(self, line):
        print('remove_link', line)

        file = open(LINKS_PATH, 'r')
        lines = file.read()
        file.close()

        lines = self._filter_lines(lines)
        res = list(filter(lambda x: x[0] != line, lines))
        res = list(map(lambda x: ", ".join(x), res))
        res = "\n".join(res)

        self._save_file(res)

    def _read_file(self):
        file = open(LINKS_PATH, 'r')
        lines = file.read()
        file.close()

        return lines

    def _save_file(self, res):
        with open(LINKS_PATH, 'w') as f:
            f.write(res)

    def _filter_lines(self, lines):
        def split(link):
            result = link.split(',')
            url = result[0].strip()
            dir = result[1].strip() if len(result) == 2 else 'other'
            flag = result[2].strip() if len(result) == 3 else ''
            return [url, dir, flag]

        lines = lines.split('\n')
        lines = list(filter(lambda x: x != '', lines))
        lines = list(filter(lambda x: x.find("TODO") == -1, lines))
        lines = list(map(lambda x: split(x), lines))

        return lines

    # def set_process_link(self, line):
    # 	print('set_processing ', line, LINKS_PATH)

    # 	# file = open(LINKS_PATH, 'r')
    # 	# lines = file.read()
    # 	# lines = self._filter_lines(lines)

    # 	line_re = re.compile(r"\n" + line + r"\n")
    # 	# line_re = re.compile(line)

    # 	with open(LINKS_PATH, 'r') as fh:
    # 		lines = fh.read()
    # 		res = line_re.findall(lines)
    # 		print(res)

    # 		# numbers = [int(match[0]) for match in line_re.findall(fh.read())]
    # 		# print(numbers)

    # 		# print(sum(numbers))

    # 	# print(lines)

    # 	# new_line = 'processing ' + line

    # 	# print(line, new_line)

    # 	# lines = re.sub("/"+line+"/", new_line, lines)
    # 	# lines = lines.replace(/line/, new_line, 1)
    # 	# print(lines)
    # 	# res = list(filter(lambda x: x[0] == line, lines))
    # 	# print(res[0])


    # def get_playlist_links(self):
    # 	filename = 'links.txt'
    # 	file = open(filename, 'r')
    # 	lines = file.read()
    # 	lines = self.__filter_lines(lines)
    # 	lines = list(filter(lambda x: x[0].find("list") != -1, lines))
    # 	file.close()

    # 	return lines

    # def append_line_in_old_file(self, url, dir):
    # 	self.__append_in_file(OLD, url, dir)

    # def append_line_in_link_file(self, url, dir):
    # 	self.__append_in_file(LINKS, url, dir)

    # def remove_first_line_in_link(self):
    # 	with open(LINKS, 'r') as fin:
    # 		data = fin.read().splitlines(True)
    # 	with open(LINKS, 'w') as fout:
    # 		fout.writelines(data[1:])

    # def __append_in_file(self, filename, url, dir):
    # 	f = open(filename, "a+")
    # 	line = url + ", " + dir + "\n"
    # 	f.write(line)
    # 	f.close()

file_service = FileService()
