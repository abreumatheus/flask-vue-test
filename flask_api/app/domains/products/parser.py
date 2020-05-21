from flask_restful import reqparse
from werkzeug.datastructures import FileStorage


parser = reqparse.RequestParser()
parser.add_argument('name', type=str, help='Name could not be converted to str', location='form')
parser.add_argument('description', type=str, help='Description could not be converted to str', location='form')
parser.add_argument('price', type=float, help='Price was not float', location='form')
parser.add_argument('promotional_price', type=float, help='Promotional price was not float', location='form')
parser.add_argument('category_id', type=int, help='Category ID was not int', location='form')
parser.add_argument('photos', type=FileStorage, help='Photo is not a file', location='files')
