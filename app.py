import os
import requests
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_session import Session
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


# config
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = 'filesystem'
app.config["SESSION_USE_SIGNER"] = True
Session(app)

CORS(app, supports_credentials=True)

# details page: similiar movie/series enpoint
@app.route('/recomendation/<string:type>/<int:movieId>/')
def recomendationsMovieTv(type, movieId):
    url = f"https://api.themoviedb.org/3/{type}/{movieId}/recommendations?language=en-US&page=1"
    headers = {
        "accept" : "application/json",
        "Authorization" : f"Bearer {TMDB_ACCESS_TOKEN}"
    }

    response = requests.get(url, headers=headers)
    return jsonify(response.json())



