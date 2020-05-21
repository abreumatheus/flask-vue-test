from flask import request
from flask_restful import Resource
from app.domains.categories.actions import CategoryActions
from app.domains.categories.schemas import CategorySchema


_CRUD_CATEGORIES = CategoryActions()
_CATEGORY_SCHEMA = CategorySchema()


class CategoriesEndpoints(Resource):
    def post(self):
        category_in = {'name': request.json['name']}
        category = _CRUD_CATEGORIES.add_new_category(category_in)
        return _CATEGORY_SCHEMA.dump(category)

    def get(self, category_id: int = None):
        if category_id:
            category = _CRUD_CATEGORIES.get_category_by_id(category_id)
            return _CATEGORY_SCHEMA.dump(category)
        categories = _CRUD_CATEGORIES.get_all_categories()
        return _CATEGORY_SCHEMA.dump(categories, many=True)

    def delete(self, category_id: int):
        _CRUD_CATEGORIES.delete_category_by_id(category_id)
        return {'msg': 'Category deleted!'}

    def put(self, category_id: int):
        category_in = {'id': category_id, 'name': request.json['name']}
        category = _CRUD_CATEGORIES.update_category(category_in)
        return _CATEGORY_SCHEMA.dump(category)
