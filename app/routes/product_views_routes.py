from flask import Blueprint, jsonify
from ..schemas.product_views_schema import ProductViewsSchema
from ..controllers import product_views_controller
from flask_jwt_extended import jwt_required

product_views_blueprint = Blueprint('product_views_blueprint', __name__)
product_views_schema = ProductViewsSchema(many=True)

@product_views_blueprint.route('/product_views', methods=['GET'])
@jwt_required()
def get_all_product_views():
    product_views_list = product_views_controller.get_all_product_views()
    result = product_views_schema.dump([
    {
        'id': product_views.id,
        'views': product_views.views,
        'product_id': product_views.product_id,
        'product_name': product.name,
        'product_price': product.price,
        'product_brand': product.brand,
        'product_sku': product.sku
    } for product_views, product in product_views_list
    ])
    return result
    