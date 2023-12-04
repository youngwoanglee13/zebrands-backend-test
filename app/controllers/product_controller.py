from ..database.db import db
from ..models.product import Product

def get_all_products()->list[Product]:
    return db.session.query(Product).all()

def get_product(product:Product)->Product:
    return db.session.query(Product).filter(Product.id==product.id).first()

def create_product(product:Product)->Product:
    db.session.add(product)
    db.session.commit()
    return product 

def update_product(product:Product) -> Product:
    upd_product = Product.query.get(product.id)
    for key, value in product.__dict__.items():
         if not key.startswith('_'):
            setattr(upd_product, key, value)
    db.session.commit()
    return upd_product    

def delete_product(product:Product)->Product:
    del_product = Product.query.get(product.id)
    db.session.delete(del_product)
    db.session.commit()
    return del_product

