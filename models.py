from config import *

class Book(db.Model):

    id = db.Column('bk_id',db.Integer(),primary_key=True)
    name = db.Column('bk_name',db.String(30))
    vender = db.Column('bk_vender',db.String(30))
    lang = db.Column('bk_lang', db.String(30))
    price = db.Column('bk_price', db.String(30))
    author = db.Column('bk_author', db.String(30))

with app.app_context():
    db.create_all()