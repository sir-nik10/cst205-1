from flask import Flask, render_template, request, redirect, url_for
from flask_dance.contrib.spotify import make_spotify_blueprint, spotify
from flask_bootstrap import Bootstrap
import requests, json, urllib.parse
from authenticate import *

app = Flask(__name__)
app.secret_key = 'development'
Bootstrap(app)

# authentication keys in authenticate.py in same dir
# (not in github repo)
# go to: https://developer.spotify.com/dashboard/applications
#blueprint = make_spotify_blueprint(
#    client_id='..client key..',
#    client_secret='..client secret..',
#    scope='playlist-modify-public streaming user-library-read',
#)

app.register_blueprint(blueprint, url_prefix='/login')

@app.route('/')
def index():
    if not spotify.authorized:
        return redirect(url_for('spotify.login'))
    search_string = urllib.parse.quote('The Birthday Party')
    resp = spotify.get(f'v1/search?q={search_string}&type=artist')
    return render_template('home.html', data=resp.json())