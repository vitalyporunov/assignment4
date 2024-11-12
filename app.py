from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from config import Config
from models import db, Pet, AdoptionApplication

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

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

@app.route('/adopt/<int:pet_id>', methods=['GET', 'POST'])
def adopt_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    if request.method == 'POST':
        full_name = request.form['full_name']
        email = request.form['email']
        phone = request.form['phone']
        address = request.form['address']
        preferences = request.form['preferences']
        
        # Save adoption application
        application = AdoptionApplication(
            full_name=full_name,
            email=email,
            phone=phone,
            address=address,
            preferences=preferences,
            pet_id=pet.id
        )
        db.session.add(application)
        db.session.commit()
        flash('Your adoption application has been submitted!', 'success')
        return redirect(url_for('home'))
    
    return render_template('adoption_form.html', pet=pet)

@app.route('/admin')
def admin_dashboard():
    pets = Pet.query.all()
    applications = AdoptionApplication.query.all()
    return render_template('admin_dashboard.html', pets=pets, applications=applications)

@app.route('/admin/pet/add', methods=['POST'])
def add_pet():
    name = request.form['name']
    breed = request.form['breed']
    age = request.form['age']
    description = request.form['description']
    image_url = request.form['image_url']

    pet = Pet(name=name, breed=breed, age=age, description=description, image_url=image_url)
    db.session.add(pet)
    db.session.commit()
    flash('New pet added successfully!', 'success')
    return redirect(url_for('admin_dashboard'))

@app.route('/admin/pet/delete/<int:pet_id>', methods=['POST'])
def delete_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    db.session.delete(pet)
    db.session.commit()
    flash('Pet deleted successfully!', 'info')
    return redirect(url_for('admin_dashboard'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Creates tables if they don't exist
    app.run(debug=True)
