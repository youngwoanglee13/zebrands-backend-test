from marshmallow import Schema, fields

class ProductSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Int(required=True)
    brand = fields.Str(required=True)
    sku = fields.Str(required=True)