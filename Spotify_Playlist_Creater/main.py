from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

HOT_100_URL = 'https://www.billboard.com/charts/hot-100'
SPOTIFY_CLIENT_ID = os.environ.get('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.environ.get('SPOTIFY_CLIENT_SECRET')

chosen_year = input('Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ')

response = requests.get(f'{HOT_100_URL}/{chosen_year}')
hot_100_web_page = response.text

soup = BeautifulSoup(hot_100_web_page, 'html.parser')
song_names = soup.select('li #title-of-a-story')
song_artists = soup.select('.a-truncate-ellipsis-2line')
song_titles = [song.getText().strip() for song in song_names]
song_artist = [song.getText().strip() for song in song_artists]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope='playlist-modify-private',
        redirect_uri='http://example.com',
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        show_dialog=True,
        cache_path='token.txt'
    )
)

user_id = sp.current_user()['id']

song_uris = []
year = chosen_year.split('-')[0]
for num in range(100):
    result = sp.search(q=f'{song_titles[num]} artist:{song_artist[num]}', type='track')
    # print(result)
    try:
        uri = result['tracks']['items'][0]['uri']
        song_uris.append(uri)
    except IndexError:
        print(f'{song_titles[num]} does\'nt exist in Spotify. Skipped.')

playlist = sp.user_playlist_create(user=user_id, name=f'{chosen_year} Billboard 100', public=False)
# print(playlist)
sp.playlist_add_items(playlist_id=playlist['id'], items=song_uris)





