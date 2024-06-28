import requests
from bs4 import BeautifulSoup
from playlist import SpotAuth
from billboard import BillboardData

# time_travel_date = input("When would you like to go? Type date in YYYY-MM-DD: ")
#
# b_data = BillboardData(time_travel_date)
# test_content = b_data.data_content
# test_bb = b_data.make_soup()
# test_songs = b_data.songs
# test_art = b_data.artists
#
# print(f"test song: {test_songs}")
# print(f"test_art: {test_art}")

auth_try = SpotAuth()
