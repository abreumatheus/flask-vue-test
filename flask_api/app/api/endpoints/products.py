from flask_restful import Resource
from app.domains.products.actions import ProductsActions
from app.domains.products.parser import parser
from app.domains.products.schema import ProductSchema


_CRUD_PRODUCTS = ProductsActions()
_PRODUCT_SCHEMA = ProductSchema()


class ProductsEndpoints(Resource):
    def post(self):
        products_args = parser.parse_args()
        product_in = {"name": products_args['name'],
                      "description": products_args['description'],
                      "price": products_args['price'],
                      "promotional_price": products_args['promotional_price'],
                      "category_id": products_args['category_id'],
                      "photos": products_args['photos']}
        product = _CRUD_PRODUCTS.add_new_product(product_in)
        return _PRODUCT_SCHEMA.dump(product)

    def get(self, product_id: str = None):
        if product_id:
            product = _CRUD_PRODUCTS.get_product_by_id(product_id)
            return _PRODUCT_SCHEMA.dump(product)
        products = _CRUD_PRODUCTS.get_all_products()
        return _PRODUCT_SCHEMA.dump(products, many=True)

    def delete(self, product_id: str):
        _CRUD_PRODUCTS.delete_product_by_id(product_id)
        return {'msg': 'Product deleted from database'}

    def put(self, product_id: str):
        products_args = parser.parse_args()
        product_in = {"id": product_id,
                      "name": products_args['name'],
                      "description": products_args['description'],
                      "price": products_args['price'],
                      "promotional_price": products_args['promotional_price'],
                      "category_id": products_args['category_id']}
        product = _CRUD_PRODUCTS.update_product(product_in)
        return _PRODUCT_SCHEMA.dump(product)
