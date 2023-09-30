from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SelectField
from wtforms.validators import InputRequired, Optional, NumberRange, URL

class CreatePetForm(FlaskForm):
    name = StringField("Pet Name", validators=[InputRequired()])
    species = SelectField("Name of Species", choices= [('cat', 'Cat'),  ('dog', 'Dog'), ('porcupine', 'Porcupine')])
    photo_url = StringField("Photo URL", validators=[Optional(), URL(require_tld= True)])
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30)])
    notes = StringField("Notes", validators=[Optional()])
    available = BooleanField("Is this pet available?")

class EditPetForm(FlaskForm):
    photo_url = StringField("Photo URL", validators=[Optional(), URL(require_tld= True)])
    notes = StringField("Notes", validators=[Optional()])
    available = BooleanField("Is this pet available?")

