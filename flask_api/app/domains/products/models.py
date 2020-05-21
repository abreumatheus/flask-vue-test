from app.main import db
from sqlalchemy.dialects import postgresql


class Product(db.Model):
    __tablename__ = 'product'

    id = db.Column(db.String(255), primary_key=True)
    category_id = db.Column(db.ForeignKey('category.id', ondelete='CASCADE'), index=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    promotional_price = db.Column(db.Float, nullable=True, default=None)
    photos = db.Column(postgresql.ARRAY(db.String), nullable=True, default=['default'])
