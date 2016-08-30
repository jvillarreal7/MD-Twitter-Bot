import urllib.request
import urllib.parse
import re
import tweepy, time
import random

#Twitter credentials
CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_KEY = ""
ACCESS_SECRET = ""
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

while True:
	#Get songs from txt file, put them into a list and shuffle
	list = []
	with open('Melodic Death Bot v1.1/playlist.txt') as f:
		list = [x.strip('\n') for x in f.readlines()]
	random.shuffle(list)

	#Loop over playlist
	for song in list:
		#Fetch YT video id of the first search result
		query_string = urllib.parse.urlencode({"search_query" : song})
		html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
		search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())

		#Print to console
		print("[" + time.ctime() + "] Song tweeted: " + song + "\nhttp://www.youtube.com/watch?v="
		 + search_results[0])

		#Tweet the song
		api.update_status(song + "\n#MelodicDeathMetal" + "\n" + "https://www.youtube.com/watch?v="
		 + search_results[0])

		#Sleep for 30 minutes
		time.sleep(1800)
