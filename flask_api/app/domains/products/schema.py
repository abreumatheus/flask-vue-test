from app.main import ma
from marshmallow import fields
from .models import Product


class ProductSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Product

    id = ma.auto_field()
    category_id = fields.Integer(dump_only=True)
    name = ma.auto_field()
    description = ma.auto_field()
    price = ma.auto_field()
    promotional_price = ma.auto_field()
    photos = ma.auto_field()
