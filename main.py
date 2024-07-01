import requests
from bs4 import BeautifulSoup
import pprint
from playlist import SpotAuth
from billboard import BillboardData

time_travel_date = input("When would you like to go? Type date in YYYY-MM-DD: ")

b_data = BillboardData(time_travel_date)
test_content = b_data.data_content
test_bb = b_data.make_soup()
song_list = b_data.songs
artist_list = b_data.artists

test_songs = ["Leave The Door Open","Peaches","alsidjhf"]
test_artists = ["Silk Sonic (Bruno Mars & Anderson .Paak)", "Justin Bieber Featuring Daniel Caesar & Giveon", "asdiufhaweui"]

# print(f"test song: {song_list}")
# print(f"test_art: {test_art}")

auth_try = SpotAuth()
song_uris = []

# track = test_songs[0]
# artist = test_art[0]
# year = time_travel_date[:4]

# Testing Error Handling
# for song in test_songs:
#     year = time_travel_date.split("-")[0]
#     song_index = test_songs.index(song)
#     artist = test_artists[song_index]
#     song_search = auth_try.song_search(song, artist, year)
#     print(f"list_song: {song}")
#     print(f"list_art: {artist}")
    # if song_search is not None:
        # song_uris.append(song_search)
    # print(song_search)
# print(song_uris)

for song in song_list:
    year = time_travel_date.split("-")[0]
    song_index = song_list.index(song)
    artist = artist_list[song_index]
    song_search = auth_try.song_search(song, artist, year)
    song_uris.append(song_search)

print(len(song_uris))
print(song_uris)

# song_search = auth_try.song_search(track, year)

# print(track)
# print(artist)
# print(year)

