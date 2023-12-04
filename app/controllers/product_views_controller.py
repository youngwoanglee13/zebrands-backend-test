from ..database.db import db
from ..models.product import Product
from ..models.product_views import ProductViews

def add_product_view(product:Product)->ProductViews:
    product_views = db.session.query(ProductViews).filter(ProductViews.product_id==product.id).first()
    if product_views==None:
        new_product_query_count = ProductViews(product_id=product.id,views=1)
        db.session.add(new_product_query_count)
        db.session.commit()
        return new_product_query_count
    product_views.views=product_views.views+1
    db.session.commit()
    return product_views

def get_all_product_views()->list:
    query_counts = db.session.query(ProductViews, Product).join(Product, ProductViews.product_id == Product.id).all()
    return query_counts