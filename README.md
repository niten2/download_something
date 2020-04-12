# You can use this app for download: #
- youtube videos
- download and convert videos to mp3 from youtube
- download playlists from youtube
- git repositories
- some files from internet

# setup #

- make install
- touch ./.env, for example:
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

## run ##
- `pipenv run python ./main.py` - process all links
- `pipenv run python ./main.py --count=one` - process one link

# tests #

make tests

# TODO #
- be able configure path - git, mp3, files, youtube_videos
- be able download git code
- be able download some files
- be able download youtube files
- be able download youtube like mp3 files
- be able download vimeo

# Youtube get all links from watch later (run in console) #
```js
let videos = document.querySelectorAll('.yt-simple-endpoint.style-scope.ytd-playlist-video-renderer');
var json = []
videos.forEach(video => {
  var url = 'https://www.youtube.com' + video.getAttribute('href');
  url = url.split('&list=WL&index=');
  url = url[0];
  json.push(url);
});
json.map(j => console.log(j));
```
