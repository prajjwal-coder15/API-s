# 

from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import requests


app = Flask(__name__)
TMDB_API_KEY = "your_api_key"  
BASE_URL = "https://api.themoviedb.org/3"
app.config["BASE_URL"] = BASE_URL
app.config["TMDB_API_KEY"] = TMDB_API_KEY

CORS(app)

# Helper function to make TMDB API requests
def fetch_tmdb_data(endpoint, params=None):
    if params is None:
        params = {}
    params["api_key"] = app.config["TMDB_API_KEY"]
    url = f"{app.config['BASE_URL']}{endpoint}"
    response = requests.get(url, params=params)
    return response.json()

@app.route("/")
def hello_from_root():
    return jsonify(message='Hello !,WELLCUMMM TO MOVIE RECUMMMONDER SYSTEM')

# Route to fetch trending movies
@app.route("/trending",methods=['GET'])
def trending_movies():
    endpoint = "/trending/movie/day"
    data = fetch_tmdb_data(endpoint)
    return jsonify(data)


# Route to fetch popular movies
@app.route("/discover",methods=['GET'])
def discover_movies():
    endpoint = "/discover/movie"
    data = fetch_tmdb_data(endpoint)
    return jsonify(data)  

# Route to fetch popular movies
@app.route("/popular",methods=['GET'])
def popular_movies():
    endpoint = "/movie/popular"
    data = fetch_tmdb_data(endpoint)
    return jsonify(data)

# Route to search for movies
@app.route("/search",methods=['GET'])
def search_movies():
    query = request.args.get("query", "")
    endpoint = "/search/movie"
    params = {"query": query}
    data = fetch_tmdb_data(endpoint, params)
    return jsonify(data)

# Route to fetch movie details
@app.route("/movie/<int:movie_id>",methods=['GET'])
def movie_details(movie_id):
    endpoint = f"/movie/{movie_id}"
    data = fetch_tmdb_data(endpoint)
    return jsonify(data)

# Route to fetch upcoming movies
@app.route("/upcoming",methods=['GET'])
def upcoming_movies():
    endpoint = "/movie/upcoming"
    data = fetch_tmdb_data(endpoint)
    return jsonify(data)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000, debug=True)
