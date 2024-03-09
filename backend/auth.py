# from flask import Blueprint, request, jsonify
# from flask_bcrypt import Bcrypt
# from flask_jwt_extended import create_access_token
# import re
# from Db import get_db;  
# import mysql.connector;

# auth_bp = Blueprint('auth', __name__)
# bcrypt = Bcrypt()

# # Regular expression for validating an Email
# email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

# @auth_bp.route('/register', methods=['POST'])
# def register():
#     data = request.get_json()
#     email = data.get('email')
#     name = data.get('name')
#     password = data.get('password')
#     # Validation checks
#     if not re.match(email_regex, email):
#         return jsonify({"msg": "Invalid email format"}), 400
#     if len(password) < 8:
#         return jsonify({"msg": "Password must be at least 8 characters long"}), 400
#     db = get_db()
#     cursor = db.cursor(dictionary=True)
#     # Check if the user already exists.
#     cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
#     existing_user = cursor.fetchone()
#     if existing_user:
#         return jsonify({"msg": "User already exists"}), 409
#     # Hash the password before storing it.
#     hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
#     # Insert the new user into the database.
#     try:
#         cursor.execute(
#             "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
#             (name, email, hashed_password)
#         )
#         db.commit()
#     except mysql.connector.Error as err:
#         db.rollback()
#         return jsonify({"msg": f"Failed to register user: {err}"}), 500
#     return jsonify({"msg": "User created successfully", "status": "success"}), 201

# @auth_bp.route('/login', methods=['POST'])
# def login():
#     print("login")
#     data = request.get_json()
#     email = data.get("email")
#     password = data.get("password")
#     # Establish a database connection
#     db = get_db()
#     cursor = db.cursor(dictionary=True)
#     # Query to find user by email
#     cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
#     user = cursor.fetchone()
#     # If user found and password matches
#     if user and bcrypt.check_password_hash(user["password"], password):
#         # Create JWT access token
#         access_token = create_access_token(identity=user["id"])
#         return jsonify(access_token=access_token), 200
#     else:
#         return jsonify({"msg": "Invalid username or password"}), 401

# # You may add more routes related to authentication here
