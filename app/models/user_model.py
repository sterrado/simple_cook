from ..db import db

class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    group_id = db.Column(db.Integer, db.ForeignKey('groups.id'))
    group = db.relationship('GroupModel', backref=db.backref('users', lazy=True))

    # Add method to hash password and verify password here
