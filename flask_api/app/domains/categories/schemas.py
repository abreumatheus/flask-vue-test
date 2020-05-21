from app.main import ma
from .models import Category


class CategorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Category
