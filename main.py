#!/bin/python
# pipenv run python ./main.py --count=all
# pipenv run python ./main.py --count=one
import argparse
from src.downloader import downloader

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--count', help='count links')
    args = parser.parse_args()
    count = args.count or 'all'

args = get_args()

if __name__ == '__main__':

    if args.count == 'all':
        while downloader.process():
            print('\n------------\n')
    elif args.count == 'one':
        downloader.process()
