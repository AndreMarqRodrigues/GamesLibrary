import mysql.connector
from flask import current_app, g
from flask.cli import with_appcontext

def get_db():
    """Establish a connection to the database and store it in Flask's 'g' global."""
    if 'db' not in g:
        g.db = mysql.connector.connect(
            host=current_app.config['MYSQL_DATABASE_HOST'],
            user=current_app.config['MYSQL_DATABASE_USER'],
            password=current_app.config['MYSQL_DATABASE_PASSWORD'],
            database=current_app.config['MYSQL_DATABASE_DB'],
        )
    return g.db

def close_db(e=None):
    """Close the database connection."""
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_app(app):
    """Register database-related teardown appcontext and other init tasks."""
    app.teardown_appcontext(close_db)
