from ..database.db import db
from sqlalchemy import ForeignKey

class ProductViews(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, ForeignKey('product.id'), nullable=False)
    views = db.Column(db.Integer, default=0, nullable=False)