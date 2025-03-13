import uuid  # Importing the UUID module to generate unique IDs for tickets
from flask_sqlalchemy import SQLAlchemy  # Importing SQLAlchemy for database handling
from flask import Flask  # Importing Flask to create the web application

# Initializing the Flask application
app = Flask(__name__)

# Configuring the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tickets.db'  # Defines the database file location
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disables modification tracking to improve performance

# Initializing the database with Flask app
db = SQLAlchemy(app)

# Defining the Ticket model (table structure)
class Ticket(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()), unique=True, nullable=False)
    # A unique identifier for each ticket, using UUID (Universally Unique Identifier)

    name = db.Column(db.String(100), nullable=False)  # Stores the name of the person submitting the ticket
    email = db.Column(db.String(100), nullable=False)  # Stores the email of the person submitting the ticket
    issue = db.Column(db.Text, nullable=False)  # Stores the description of the issue
    status = db.Column(db.String(20), default="open")  # Stores the ticket status (default is "open")

# Creating the database when the script runs
if __name__ == "__main__":
    with app.app_context():  # Ensures the database is created within the Flask application context
        db.create_all()  # Creates the tables in the database if they don't exist
        print("The Database has been created!")  # Prints a confirmation message
