# Ian Annase
# 4/16/18

import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError

# Get the username from terminal
username = sys.argv[1]

#get user id 121928206

# Erase cache adn prompt for user permission
try:
    token = util.prompt_for_user_token(username)
except:
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username)

#Create our spotifyObject

spotifyObject = spotipy.Spotify(auth=token)