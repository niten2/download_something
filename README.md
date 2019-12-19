# you can use this app for download something #
- youtube videos
- download and convert videos to mp3 from youtube
- download playlists from youtube
- git repositories
- some files from internet

# setup #

- pipenv install
- touch .env, for example:
```
git_path=/home/{{user}}/_test/git
video_path=/home/{{user}}/_test/video
mp3_path=/home/{{user}}/_test/mp3
links_path=/home/{{user}}/_test/links.txt
log_path=/home/{{user}}/_test/log.txt
```
- add links to file by links_path, for example:
```
https://www.youtube.com/watch?v=FCSAqFE1avk, go
https://www.youtube.com/watch?v=FCSAqFE1avk, go, mp3
https://www.youtube.com/playlist?list=PLrCZzMib1e9q-X5V9pTM6J0AemRWseM7I, golang, playlist
http://temp-cdn.datalock.ru/filename.mp4, some-dir
https://github.com/ema2159/centaur-tabs, git-dir
```
- run `pipenv run python ./main.py`
- you can add alias or crone tack

# tests #

pipenv run python -m unittest discover

# list TODO #
- app be able configure path - git, mp3, files, youtube_videos
- app be able download git code
- app be able download some files
- app be able download youtube files
- app be able download youtube like mp3 files
