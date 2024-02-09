from ..db import db

class InvoiceModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    purchase_order_id = db.Column(db.Integer, db.ForeignKey('purchaseordermodel.id'))
    # Define relationships and additional fields
