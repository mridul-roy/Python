import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth


requested_date = input("Which year do you want to travel to? Type the date in this formate YY-MM-DD :")

URL = ("https://www.billboard.com/charts/hot-100/" + requested_date)
response = requests.get(URL)
top100_songs = response.text

soup = BeautifulSoup(top100_songs, "html.parser")


songs_name_span = soup.select(selector="li ul li h3")

songs_name = [song.getText().strip() for song in songs_name_span]


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://open.spotify.com/",
        client_id="4473f78b817d430597550f84cfc188a1",
        client_secret="be94629f0ce44a7681ed90903619bd81",
        show_dialog=True,
        cache_path="token.txt",
        username="Mridul Roy",
    )
)
user_id = sp.current_user()["id"]












print(songs_name)