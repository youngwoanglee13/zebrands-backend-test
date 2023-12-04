from marshmallow import Schema, fields

class ProductViewsSchema(Schema):
    id = fields.Int(dump_only=True)
    product_id = fields.Int(required=True)
    views = fields.Int(required=True)
    product_name = fields.Str(required=True)
    product_price = fields.Int(required=True)
    product_brand = fields.Str(required=True)
    product_sku = fields.Str(required=True)