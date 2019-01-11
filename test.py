# Ethan Tuckman
# project_sandpiper
# January 10, 2019

#Ethan's Spotify user ID: 121928206

import os
import sys
import pprint
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError

# Get the username from terminal
if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print("Usage: %s username/userID" %(sys.argv[0],))
    sys.exit()

#set token and scope
#Scopes provide Spotify users using third-party apps the confidence that only the information they choose to share will be shared
scope = ''
token = util.prompt_for_user_token(username,scope)

if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    results = sp.current_user_playlists(limit=50)
    for i, item in enumerate(results['items']):
        print("%d %s" %(i, item['name']))
else:
    print("Can't get token for", username)



#########################################################

#had to manually upgrade version of spotipy by downloading directly from github
#before that we used this code as a workaround:

""" # Erase cache and prompt for user permission
try:
    token = util.prompt_for_user_token(username,scope)
except:
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username,scope)

print("we made it!")

#Create our spotifyObject
spotifyObject = spotipy.Spotify(auth=token) """