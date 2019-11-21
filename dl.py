#!/usr/bin/env python

"""
Author: Phil Albu
License: MIT

Usage: python dl.py

The CS7637 class videos are split up into 5 parts with
their playlist id's listed below. You must put in your own 
API key in a .env file in the form
YT_API_KEY=my_yt_api_key  (obtained from the GCP Console)
https://console.developers.google.com/apis/dashboard

See README.md for details on how to obtain an API key.

Enjoy!
"""

import youtube_dl
from youtube_api import YouTubeDataAPI
import os

from dotenv import load_dotenv
load_dotenv()

API_KEY=os.getenv('YT_API_KEY')
playlists = [
    { 'title': 'Part1', 'playlist_id': 'PLAwxTw4SYaPkdANSntXhY0btWkpPglDGD'},
    { 'title': 'Part2', 'playlist_id': 'PLAwxTw4SYaPkbpTYapAPkmAG4CX6c4zbe'},
    { 'title': 'Part3', 'playlist_id': 'PLAwxTw4SYaPnfBiz7qzbPX27x4zBBNrY5'},
    { 'title': 'Patt4', 'playlist_id': 'PLAwxTw4SYaPmYv73ffQ7TE3sZXA38EFkx'},
    { 'title': 'Part5', 'playlist_id': 'PLAwxTw4SYaPm4zEWxZ-rlepIlLUTCORcn'},
]
yt = YouTubeDataAPI(API_KEY)

# First, create a "downloads" folder if it does not exist
root_dir = os.getcwd()
downloads_dir = os.path.join(root_dir, 'downloads')
if not os.path.exists(downloads_dir):
    os.mkdir(downloads_dir)
os.chdir(downloads_dir)

# For each playlist in the array,
# create a directory inside downloads and
# download each video into that directory
for playlist in playlists:
    playlist_dir = playlist['title']
    if not os.path.exists(playlist_dir):
        os.mkdir(playlist_dir)

    # Change directory so that we can save the videos in the proper place
    os.chdir(playlist_dir)

    # Download all episodes for this playlist
    playlist = yt.get_videos_from_playlist_id(playlist['playlist_id'])
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

