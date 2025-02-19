from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class StoreModel(db.Model):
    id = db.Column(db.String(80), primary_key = True)
    name = db.Column(db.String(80), nullable = False)