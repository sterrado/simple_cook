from ..db import db

class EmployeeModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    school_id = db.Column(db.Integer, db.ForeignKey('schoolmodel.id'))
    school = db.relationship('SchoolModel', back_populates='employees')
    # Additional fields as needed
