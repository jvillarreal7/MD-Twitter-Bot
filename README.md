# MD-Twitter-Bot
Python script that tweets YouTube links to songs based on a plain text playlist.

https://twitter.com/MelodeathBot (currently running 1.1)

#Version 1.0 (Aug 28 2016):
* Loops over song titles from a .txt file.

* Sends a search query to YouTube containing the artist + song title and recieves video ID of the first result.

* Tweets artist, song title, hashtag and YouTube link periodically (default: 30 minutes).


#Version 1.1 (Aug 29 2016):
* Added a main infinite loop so the script doesn't need to be restarted after going through all the songs.

* Songs are now loaded into a list and reshuffled at the beginning of each main loop iteration.

* Console printer now shows a timestamp.

#Known issues:
* It may tweet an album instead of a song if both have the same title.
