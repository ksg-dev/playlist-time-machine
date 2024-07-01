# Responsible for interacting w Spotify and Spotipy API
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv
from pprint import pprint
from thefuzz import fuzz


load_dotenv()


class SpotAuth:
    def __init__(self):
        self._client_id = os.environ["SPOTIFY_CLIENT_ID"]
        self._client_secret = os.environ["SPOTIFY_SECRET"]
        self.request_uri = "http://example.com"
        self.scope = "playlist-modify-private"
        # self.session = self.auth()
        self.current_user = self.auth().current_user()

    def auth(self):
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=self._client_id,
            client_secret=self._client_secret,
            redirect_uri=self.request_uri,
            scope=self.scope
        ))
        # curr_user = sp.current_user()
        # print(sp.me())
        return sp

    def song_search(self, track, artist, year):
        query_str = f"track: {track} artist: {artist} year: {year}"
        result = self.auth().search(query_str, limit=1)
        # pprint(result)
        song_artist = result["tracks"]["items"][0]["artists"][0]["name"]
        song_track = result["tracks"]["items"][0]["name"]
        song_uri = result["tracks"]["items"][0]["uri"]
        # print(song_artist)
        # print(song_track)
        sim_ratio_song = fuzz.partial_ratio(track, song_track)
        sim_ratio_art = fuzz.partial_ratio(artist, song_artist)
        check_song = f"list_track: {track}\nresult_track: {song_track}\nsong_ratio: {sim_ratio_song}"
        check_artist = f"list_art: {artist}\nresult_art: {song_artist}\nart_ratio: {sim_ratio_art}"
        print(check_song)
        print(check_artist)
        print("--------------------")
        # pprint(song_uri)
        # return song_uri
