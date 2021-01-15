import json
import re
import requests
import urllib.request

artist = input('Artist name: ')
song_name = input('Song name: ')

def search_youtube():
	search_query = artist.replace(' ', '+') + '+' + song_name.replace(' ', '+')
	html = urllib.request.urlopen('https://www.youtube.com/results?search_query=' + search_query)
	video_ids = re.findall(r'watch\?v=(\S{11})', html.read().decode())
	video = 'https://youtube.com/watch?v=' + video_ids[0]
	return video

print(search_youtube())