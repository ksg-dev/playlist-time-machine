from playlist import SpotAuth
from billboard import BillboardData

time_travel_date = input("When would you like to go? Type date in YYYY-MM-DD: ")

b_data = BillboardData(time_travel_date)
test_content = b_data.data_content
test_bb = b_data.make_soup()
song_list = b_data.songs
artist_list = b_data.artists

auth_try = SpotAuth()
song_uris = []

for song in song_list:
    year = time_travel_date.split("-")[0]
    song_index = song_list.index(song)
    artist = artist_list[song_index]
    song_search = auth_try.song_search(song, artist, year)
    song_uris.append(song_search)


playlist_name = f"{time_travel_date} Billboard 100"
new_playlist_id = auth_try.create_playlist(playlist_name)

auth_try.add_songs(new_playlist_id, song_uris)
