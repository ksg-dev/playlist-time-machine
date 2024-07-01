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
        artists = self.artist_list(result)
        best_ratio = max(self.fuzzy_check(artist, artists))
        song_track = result["tracks"]["items"][0]["name"].title()
        sim_ratio_song = fuzz.partial_ratio(track.title(), song_track)
        song_uri = result["tracks"]["items"][0]["uri"]
        if best_ratio > 70 and sim_ratio_song > 70:
            return song_uri
            # print(f"{best_ratio}--list_artist: {artist}")
            # print(f"{sim_ratio_song}-- list_track: {track}\nresult_track: {song_track}")
        # print(best_ratio, sim_ratio_song)
        # print(artists)
        # print(best_ratio)

        # print(song_artist)
        # print(song_track)

        # pprint(song_uri)
        # return song_uri

    def artist_list(self, data):
        check_list = data["tracks"]["items"][0]["artists"]
        art_list = [item["name"] for item in check_list]
        return art_list

    def fuzzy_check(self, target_artist, artists_list):
        art_ratios = []
        for item in artists_list:
            sim_ratio_art = fuzz.partial_ratio(target_artist.lower(), item.lower())
            art_ratios.append(sim_ratio_art)
        # print(art_ratios)
        return art_ratios

