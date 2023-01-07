import json
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models import create_tables, Publisher, Book, Shop, Stock, Sale

models = {'publisher': Publisher, 'book': Book, 'shop': Shop, 'stock': Stock, 'sale': Sale}

DSN = "postgresql://postgres:postgres@localhost:5432/bookstore"
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()
# решение подсмотрел в примере реализации и немного переделал как мне понятнее
with open('fixtures/tests_data.json', 'r') as data_file:
    data = json.load(data_file)
for row_data in data:
    # print(row_data['model'], row_data['pk'], row_data['fields'])
    row = models[row_data['model']](id=row_data['pk'], **row_data['fields'])
    session.add(row)
session.commit()

publisher = input('Введите имя автора: ')
for s in session.query(Sale).join(Stock.sales).all():
    print(s)

session.close()
