from app import db

class Destination(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    location = db.Column(db.String(100))
    date = db.Column(db.Date)
    budget = db.Column(db.Float)
    ratings = db.Column(db.Float)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'location': self.location,
            'date': str(self.date),
            'budget': self.budget,
            'ratings': self.ratings
        }

class Itinerary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    destination_id = db.Column(db.Integer, db.ForeignKey('destination.id'), nullable=False)
