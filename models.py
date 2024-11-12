from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Pet(db.Model):
    __tablename__ = 'pets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    breed = db.Column(db.String(50))
    age = db.Column(db.Integer)
    description = db.Column(db.Text)
    image_url = db.Column(db.String(100))
    status = db.Column(db.String(20), default="Available")

    def __repr__(self):
        return f"<Pet {self.name}, Breed: {self.breed}, Age: {self.age}>"

class AdoptionApplication(db.Model):
    __tablename__ = 'adoption_applications'
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    address = db.Column(db.Text, nullable=False)
    preferences = db.Column(db.Text)
    pet_id = db.Column(db.Integer, db.ForeignKey('pets.id'), nullable=False)

    pet = db.relationship('Pet', backref=db.backref('applications', cascade="all, delete-orphan"))

    def __repr__(self):
        return f"<Application from {self.full_name} for Pet ID: {self.pet_id}>"
