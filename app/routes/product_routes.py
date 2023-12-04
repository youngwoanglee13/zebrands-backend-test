from flask import Blueprint

product_blueprint = Blueprint('product_blueprint', __name__)

@product_blueprint.route('/products', methods=['GET'])
def get_all_products():
    return "products"