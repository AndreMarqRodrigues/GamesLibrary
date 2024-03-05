from flask import Flask, jsonify, send_from_directory, request
from flask_bcrypt import Bcrypt;
from flask_jwt_extended import create_access_token, JWTManager, get_jwt_identity, jwt_required, verify_jwt_in_request;
from flask_pymongo import PyMongo;
from flask_cors import CORS;
from Db import get_db;
import mysql.connector;
import re;
import os;


app = Flask(__name__)
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'User1'
app.config['MYSQL_DATABASE_PASSWORD'] = 'pass123'
app.config['MYSQL_DATABASE_DB'] = 'GamingLib'
bcrypt = Bcrypt(app)
# Ensure you have set the secret key for your application
app.config['JWT_SECRET_KEY'] = '4e5b8f6df8ee4986ae81dfb2731ca975'
# Initialize JWTManager with your Flask app
jwt = JWTManager(app)

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

#Login route
@app.route('/login', methods=['POST'])
def login():
    print("login")
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")
    # Establish a database connection
    db = get_db()
    cursor = db.cursor(dictionary=True)
    # Query to find user by email
    cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
    user = cursor.fetchone()
    # If user found and password matches
    if user and bcrypt.check_password_hash(user["password"], password):
        # Create JWT access token
        access_token = create_access_token(identity=user["id"])
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"msg": "Invalid username or password"}), 401
    

# Regular expression for validating an Email
email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    

@app.route('/register', methods=['POST'])
def register():
    print("register")
    data = request.get_json()
    email = data.get('email')
    name = data.get('name')
    password = data.get('password')
    # Validation checks
    if not re.match(email_regex, email):
        return jsonify({"msg": "Invalid email format"}), 400
    if len(password) < 8:
        return jsonify({"msg": "Password must be at least 8 characters long"}), 400

    db = get_db()
    cursor = db.cursor(dictionary=True)

    # Check if the user already exists.
    cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
    existing_user = cursor.fetchone()
    if existing_user:
        return jsonify({"msg": "User already exists"}), 409
    # Hash the password before storing it.
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    # Insert the new user into the database.
    try:
        cursor.execute(
            "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
            (name, email, hashed_password)
        )
        db.commit()
    except mysql.connector.Error as err:
        db.rollback()
        return jsonify({"msg": f"Failed to register user: {err}"}), 500
    return jsonify({"msg": "User created successfully", "status": "success"}), 201

# The GET and POST route handler
@jwt_required()  # Make sure to protect the route
@app.route('/games', methods=['GET', 'POST'])
def all_games():
    print("game")
    verify_jwt_in_request()
    current_user_id = get_jwt_identity()  # Retrieve the user ID from the token
    app.logger.info(current_user_id)
    db = get_db()
    cursor = db.cursor(dictionary=True)
    if request.method == "POST":
        # Processing POST request
        post_data = request.get_json()
        title = post_data.get('title')
        genre = post_data.get('genre', '')
        playTime = post_data.get('playTime', 0)
        played = post_data.get('played', False)
        userId = current_user_id
        # Inserting game into MySQL
        insert_query = """
        INSERT INTO games (title, genre, playTime, played, userId) 
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(insert_query, (title, genre, playTime, played, userId))
        db.commit()
        return jsonify({'message': 'Game added successfully!'}), 201
    else:
        # Processing GET request
        # Retrieving all games from MySQL
        cursor.execute("SELECT * FROM games WHERE userId = %s", (current_user_id,))  # Filter by userId
        games = cursor.fetchall()
        print("O print esta aqui:")
        print (games)
        print(current_user_id)
        return jsonify({'status': 'success', 'games': games}), 200


#The PUT and DELETE routes
@app.route('/games/<game_id>', methods=['PUT', 'DELETE'])
@jwt_required()
def single_game(game_id):
    db = get_db()
    cursor = db.cursor(dictionary=True)
    current_user_id = get_jwt_identity()
    if request.method == 'PUT':
        post_data = request.get_json()
        title = post_data.get('title')
        genre = post_data.get('genre', None)
        playTime = post_data.get('playTime', 0)
        played = post_data.get('played', False)
        # Ensure you convert 'played' to an integer (1 for True, 0 for False) if your database expects an INT for BOOLEAN
        played_int = 1 if played else 0
        update_query = """
        UPDATE games SET title=%s, genre=%s, playTime=%s, played=%s 
        WHERE id=%s AND userId=%s
        """
        cursor.execute(update_query, (title, genre, playTime, played_int, game_id, current_user_id))
        db.commit()
        if cursor.rowcount:
            return jsonify({'status': 'success', 'message': 'Game updated!'}), 200
        else:
            return jsonify({'status': 'failure', 'message': 'Game not found or you do not have permission to update it.'}), 404
    elif request.method == 'DELETE':
        delete_query = "DELETE FROM games WHERE id=%s AND userId=%s"
        cursor.execute(delete_query, (game_id, current_user_id))
        db.commit()
        if cursor.rowcount:
            return jsonify({'status': 'success', 'message': 'Game removed!'}), 200
        else:
            return jsonify({'status': 'failure', 'message': 'Game not found or you do not have permission to delete it.'}), 404



#Removing the game to update
def remove_game(game_id):
    for game in games:
        if game['id'] == str(game_id):  # Cast to int if IDs are integers
            games.remove(game)
            return True
    return False

if __name__ == '__main__':
    app.run(debug=True)