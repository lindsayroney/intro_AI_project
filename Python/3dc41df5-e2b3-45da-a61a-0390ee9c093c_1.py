import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id = 'your_client_id'
client_secret = 'your_client_secret'

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
