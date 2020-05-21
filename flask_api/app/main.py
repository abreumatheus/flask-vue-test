from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_swagger_ui import get_swaggerui_blueprint
from .core import config


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)
db = SQLAlchemy(app)
api = Api(app)
ma = Marshmallow(app)

SWAGGER_URL = ''  # URL for exposing Swagger UI (without trailing '/')
API_URL = 'http://localhost:7000/static/openapi.json'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Test application"
    }
)

# Register blueprint at URL
# (URL must match the one given to factory function above)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

from .api.endpoints.products import ProductsEndpoints
from .api.endpoints.categories import CategoriesEndpoints

api.add_resource(ProductsEndpoints, '/products', '/products/<product_id>', endpoint='products')
api.add_resource(CategoriesEndpoints, '/categories', '/categories/<int:category_id>', endpoint='categories')
