from app.main import db


class Category(db.Model):
    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

    products = db.relationship('Product', primaryjoin='Category.id == Product.category_id',
                               backref='category')
