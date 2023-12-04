from ..database.db import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    brand = db.Column(db.String(100), nullable=False)
    sku = db.Column(db.String(100), nullable=False)
