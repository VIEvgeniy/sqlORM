import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

class publisher(Base):
    __tablename__ = 'publisher'

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40), unique=True)

class book(Base):
    __tablename__ = 'book'

    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String(length=40), unique=True)
    id_publicher = sq.Column(sq.Integer, sq.ForeignKey("publisher.id"), nullable=False)
    publicher = relationship(publisher, backref='publisher')

class shop(Base):
    __tablename__ = 'shop'

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40), unique=True)

class stock(Base):
    __tablename__ = 'stock'

    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String(length=40), unique=True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey("book.id"), nullable=False)
    id_shop = sq.Column(sq.Integer, sq.ForeignKey("shop.id"), nullable=False)
    book = relationship(publisher, backref='book')
    shop = relationship(publisher, backref='shop')
    count = sq.Column(sq.Integer)

class sale(Base):
    __tablename__ = 'sale'

    id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.Integer)
    date_sale = sq.Column(sq.Date)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey("stock.id"), nullable=False)
    stock = relationship(publisher, backref='stock')
    count = sq.Column(sq.Integer)

def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)