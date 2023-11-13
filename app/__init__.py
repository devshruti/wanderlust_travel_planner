from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the database - replace 'your_database_uri' with your actual database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///wanderlust.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Import models to create tables
from app import models

# Blueprint registration for routes
from app.routes.destinations import destination_bp

app.register_blueprint(destination_bp)

if __name__ == '__main__':
    app.run(debug=True)
