# bolly

Using local files in /media, make a movie from them as follows:

Scoop up all image files in timestamp order and turn it into a very simple video, with each image shown for some frames over a couple of seconds.

The video file will be written back to disk and called bolly.mp4.

For now, just processes images. Adding audio might be a future feature. 

----

# handy commands in using docker

docker image ls --digests
docker cp <docker-image-name>:/media/bolly.mp4 .

Install editor in docker image:
apt-get install vim
apt-get install vim-tiny

