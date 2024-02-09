from ..db import db

class PurchaseOrderModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    school_id = db.Column(db.Integer, db.ForeignKey('schoolmodel.id'))
    supplier_id = db.Column(db.Integer, db.ForeignKey('suppliermodel.id'))
    # Define relationships and additional fields
