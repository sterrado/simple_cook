from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class GroupModel(db.Model):
    __tablename__ = 'groups'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
