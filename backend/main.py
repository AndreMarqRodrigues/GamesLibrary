from flask import Flask, jsonify, send_from_directory, request
from flask_cors import CORS
import os
import uuid

app = Flask(__name__)


app.config.from_object(__name__)

CORS(app, resources={r"/*": {
    "origins": "*",
    "allow_headers": ["Content-Type", "Authorization"],
    "supports_credentials": True
}})


# Handle VueRouter history mode
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return send_from_directory(os.path.join(app.root_path, 'static'), 'index.html')


# hello world Route
@app.route('/', methods=['GET'])
def greetings():
    return("Hello, world!")


@app.route('/shark', methods=['GET'])
def shark():
    return("12313!")

games = [
    {
        'id' : str(uuid.uuid4()),
        'title' : 'Evil Within',
        'genre':'horror',
        'played': False
    },
    {
        'id' : str(uuid.uuid4()),
        'title' : 'League Of Legends',
        'genre':'MOBA',
        'played': True
    },
    {
        'id' : str(uuid.uuid4()),
        'title' : 'Forza Horizon',
        'genre':'racing',
        'played': True
    },
    {
        'id' : str(uuid.uuid4()),
        'title' : 'Minecraft',
        'genre':'survival',
        'played': False
    },
    {
        'id' : str(uuid.uuid4()),
        'title' : 'The last of us',
        'genre':'survival',
        'played': False
    }
]

# The GET and POST route handler
@app.route('/games', methods=['GET', 'POST'])
def all_games():
    response_object = {'status': 'success'}
    if request.method == "POST":
        # Processing POST request
        post_data = request.get_json()
        games.append({
            'id' : uuid.uuid4().hex,
            'title': post_data.get('title'),
            'genre': post_data.get('genre'),
            'played': post_data.get('played', False)  # Default to False if not provided
        })
        response_object['message'] = 'Game  added!'
    else:
        # Processing GET request
        response_object['games'] = games
        response_object['message'] = 'Games retrieved!'
    return jsonify(response_object)

#The PUT and DELETE routes
@app.route('/games/<game_id>', methods=['PUT', 'DELETE'])
def single_game(game_id):
    # Find the game
    game = next((g for g in games if g['id'] == game_id), None)
    if request.method == 'PUT':
        if game:
            post_data = request.get_json()
            # Update game's details with post_data
            game['title'] = post_data.get('title', game['title'])
            game['genre'] = post_data.get('genre', game['genre'])
            game['played'] = post_data.get('played', game['played'])
            return jsonify({'status': 'success', 'message': 'Game updated!', 'game': game})
        else:
            return jsonify({'status': 'failure', 'message': 'Game not found.'}), 404
    elif request.method == 'DELETE':
        if game:
            # Remove the game from the list
            games[:] = [g for g in games if g['id'] != game_id]
            return jsonify({'status': 'success', 'message': 'Game removed!'})
        else:
            return jsonify({'status': 'failure', 'message': 'Game not found.'}), 404


#Removing the game to update
def remove_game(game_id):
    for game in games:
        if game['id'] == str(game_id):  # Cast to int if IDs are integers
            games.remove(game)
            return True
    return False



if __name__ == "__main__":
    app.run(debug=True) 