import json
import os
import re
import requests
import urllib.request

from pytube import YouTube


artist = input('Artist Name: ')
song_name = input('Song Name: ')

def search_youtube():
	search_query = artist.replace(' ', '+') + '+' + song_name.replace(' ', '+')
	html = urllib.request.urlopen('https://www.youtube.com/results?search_query=' + search_query)
	video_ids = re.findall(r'watch\?v=(\S{11})', html.read().decode())
	video = 'https://youtube.com/watch?v=' + video_ids[0]
	return video


def download_video():
	print('starting audio download...')
	yt = YouTube(search_youtube())
	t = yt.streams.filter(only_audio=True)
	t[0].download('./audio')
	print('done downloading')


def find_file():
	download_video()
	os.chdir('./audio')
	file = os.listdir()[0]
	global file_name
	file_name = song_name.replace(' ', '_') + '.wav'
	os.rename(file, file_name)
	file = os.listdir()[0]
	os.chdir('..')
	return file


find_file()