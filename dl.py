#!/usr/bin/env python

"""
Author: Phil Albu
License: MIT

Usage: python dl.py

The CS7637 class videos are split up into 5 parts with
their playlist id's listed below. You must put in your own API
key below.

Enjoy!
"""

import youtube_dl
from youtube_api import YouTubeDataAPI
import os

API_KEY='Your-Key-Here'
parts = [
    { 'part': 1, 'playlist_id': 'PLAwxTw4SYaPkdANSntXhY0btWkpPglDGD'},
    { 'part': 2, 'playlist_id': 'PLAwxTw4SYaPkbpTYapAPkmAG4CX6c4zbe'},
    { 'part': 3, 'playlist_id': 'PLAwxTw4SYaPnfBiz7qzbPX27x4zBBNrY5'},
    { 'part': 4, 'playlist_id': 'PLAwxTw4SYaPmYv73ffQ7TE3sZXA38EFkx'},
    { 'part': 5, 'playlist_id': 'PLAwxTw4SYaPm4zEWxZ-rlepIlLUTCORcn'},
]
yt = YouTubeDataAPI(API_KEY)

root_dir = os.getcwd()
for part in parts:
    part_dir = 'Part' + str(part['part'])
    if not os.path.exists(part_dir):
        os.mkdir(part_dir)
    if part['part'] < 3:
        continue

    # Change directory so that we can save the videos in the proper place
    os.chdir(part_dir)

    # Download all episodes for this part
    playlist = yt.get_videos_from_playlist_id(part['playlist_id'])
    for videoix, v in enumerate(playlist):
        try:
            video = yt.get_video_metadata(v['video_id'])
            title = str(videoix) + '. ' + video['video_title']
            link = 'http://youtube.com/watch?v=' + video['video_id']
            try:
                with youtube_dl.YoutubeDL({'outtmpl': str(videoix+1) + '. %(title)s.%(ext)s'}) as ydl:
                    result = ydl.download([link])
            except Exception as e:
                print("Exception on download: %s" % e)
        except Exception as e:
            print("Exception on get_video_metadata: %s" % e)

    # Switch back to the root dir of project
    os.chdir(root_dir)

