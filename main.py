#!/bin/python
# pipenv run python ./main.py
from src.downloader import downloader

if __name__ == '__main__':
    while downloader.process():
        print('\n------------\n')
