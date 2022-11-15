from sqlalchemy import create_engine
from models.hero import Hero
from models.item import Item
from sqlmodel import SQLModel, create_engine


def create_db_and_tables(engine):
    SQLModel.metadata.create_all(engine)


def main():
    engine = create_engine("sqlite:///../data/database.db", echo=True)
    create_db_and_tables(engine)


if __name__ == '__main__':
    main()
