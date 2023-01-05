import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models import create_tables

DSN = "postgresql://postgres:postgres@localhost:5432/bookstore"
engine = sqlalchemy.create_engine(DSN)

Session = sessionmaker(bind=engine)
session = Session()

create_tables(engine)

session.commit()
session.close()
