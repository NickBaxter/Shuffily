print("Welcome to my spotify play list program")
name = raw_input("What artist would you like to search for?\n")

import spotipy
spotify = spotipy.Spotify()
results = spotify.search(q='artist:' + name, type='artist')
print results
