from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# MySQL configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@host/database_name'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import models to create tables
from app import models

# Register routes (e.g., destinations, itineraries, expenses)
from app.routes.destinations import destination_bp
from app.routes.itineraries import itinerary_bp
from app.routes.expenses import expense_bp

app.register_blueprint(destination_bp)
app.register_blueprint(itinerary_bp)
app.register_blueprint(expense_bp)

if __name__ == '__main__':
    app.run(debug=True)
