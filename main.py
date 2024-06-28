import requests
from bs4 import BeautifulSoup

# time_travel_date = input("When would you like to go? Type date in YYYY-MM-DD: ")

test_date = "2021-05-05"
root_url = "https://www.billboard.com/charts/hot-100/"
SONG_CLASS_STR = "c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only"
# ARTIST_CLASS_STR = "c-label  a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only"
ARTIST_CLASS_STR = "c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only"

TARGET_URL = f"{root_url}{test_date}"

response = requests.get(TARGET_URL)
content = response.text
# print(content)

soup = BeautifulSoup(content, "html.parser")
all_song_titles = soup.find_all(name="h3", class_=SONG_CLASS_STR)
all_artists = soup.find_all(name="span", class_=ARTIST_CLASS_STR)
# print(all_artists)

song_titles = [song.getText().strip() for song in all_song_titles]
artists = [artist.getText().strip() for artist in all_artists]

print(song_titles)
print(artists)

