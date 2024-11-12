from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/pet_shelter'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Pet model
class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    breed = db.Column(db.String(50))
    age = db.Column(db.Integer)
    description = db.Column(db.Text)
    image_url = db.Column(db.String(100))
    status = db.Column(db.String(20), default="Available")

# Define the main routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/pets')
def pets():
    pets = Pet.query.all()
    return render_template('pets.html', pets=pets)

@app.route('/pet/<int:pet_id>')
def pet_profile(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    return render_template('pet_profile.html', pet=pet)

@app.route('/adopt/<int:pet_id>', methods=['POST'])
def adopt_pet(pet_id):
    # Handle adoption form submission logic here
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
