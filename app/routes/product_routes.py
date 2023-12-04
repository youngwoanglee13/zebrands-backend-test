from flask import Blueprint, jsonify, request
from ..models.product import Product
from ..schemas.product_schema import ProductSchema
from ..controllers import product_controller

product_blueprint = Blueprint('product_blueprint', __name__)
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

@product_blueprint.route('/products', methods=['GET'])
def get_all_products():
    products = product_controller.get_all_products()
    return jsonify(products_schema.dump(products))

@product_blueprint.route('/products', methods=['POST'])
def create_product():
    product_data = product_schema.load(request.json)
    new_product = Product(**product_data)
    added_student = product_controller.create_product(new_product)
    return jsonify(product_schema.dump(added_student))

@product_blueprint.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    product_data = product_schema.load(request.json, partial=True)
    product_data['id'] = id
    product = Product(**product_data)
    updated_product = product_controller.update_product(product)
    return jsonify(product_schema.dump(updated_product))

@product_blueprint.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product(id=id)
    deleted_product = product_controller.delete_product(product)
    return jsonify(product_schema.dump(deleted_product))

@product_blueprint.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    product = Product(id=id)
    product = product_controller.get_product(product)
    return jsonify(product_schema.dump(product))
