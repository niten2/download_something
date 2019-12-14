#!/bin/python
from src.file_service import file_service
from src.downloader import downloader

if __name__ == '__main__':
	links = file_service.get_links()
	downloader.run(links)
