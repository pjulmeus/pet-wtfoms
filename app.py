from flask import Flask, request, redirect, render_template
from models import db, connect_db, Pet
from flask_debugtoolbar import DebugToolbarExtension
from forms import CreatePetForm, EditPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "oh-so-secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

connect_db(app)
db.drop_all()
db.create_all()

@app.route('/')
def pet_home():
    """List all the pets and links us to an add pet page"""
    pet = Pet.query.all()
    return render_template("home.html", pet = pet)

@app.route('/add', methods = ["GET", "POST"])
def add_pet_form():
    """Get a create a form, create a pet object, post form data on home page"""
    form = CreatePetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        available = form.available.data
        pet = Pet(name = name, species = species, photo_url= photo_url, age = age, notes = notes, available= available)
        db.session.add(pet)
        db.session.commit()
        return redirect("/")   
    else:
        return render_template("add_pet.html", form = form)
    
@app.route('/pets/<int:pet_id>', methods = ["GET", "POST"])
def edit_pet_form(pet_id):
    """Show pet details, and update pet detail and sned to homepage"""
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm()
    if form.validate_on_submit():
        photo_url = form.photo_url.data
        notes = form.notes.data
        available = form.available.data

        if photo_url:
            pet.photo_url = photo_url
        if notes:
            pet.notes = notes
        if available:
            pet.available = available
        db.session.commit()
        return redirect(f"/pets/{pet_id}")
    else:   
            return render_template("pet_detail.html", pet =pet, form= form)


