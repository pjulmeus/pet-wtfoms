from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connect to database."""
    db.app = app
    db.init_app(app)

class Pet(db.Model):
    __tablename__ = "pets"

    # def __repr__(self):
    #     p = self
    #     return f" Hello my name is {p.first_name} {p.last_name}, here is my user picture {p.image_url}"
    
    # def get_first_name(cls, first_name):
    #  return cls.query.filter(first_name)
    
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    name = db.Column(db.String(50),
                     nullable=False,
                     unique=True)
    species = db.Column(db.String)
    photo_url = db.Column(db.String, nullable=True)
    age = db.Column(db.Integer, nullable = True)
    notes = db.Column(db.String, nullable=True)
    available = db.Column(db.Boolean, nullable = False)

