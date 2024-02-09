from ..db import db

class SchoolModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    employees = db.relationship('Employee', backref='school', lazy=True)
    # Additional fields as needed
