from sqlalchemy import create_engine
from models.hero import Hero
from sqlmodel import Session, SQLModel, create_engine, select


def create_db_and_tables(engine):
    SQLModel.metadata.create_all(engine)


def insert_heroes(engine):
    hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")
    hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
    hero_3 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)
    with Session(engine) as session:
        session.add(hero_1)
        session.add(hero_2)
        session.add(hero_3)
        session.commit()


def select_heroes(engine):
    with Session(engine) as session:
        statement = select(Hero).where(Hero.name == "Spider-Boy")
        hero_list = session.exec(statement).all()
        for hero in hero_list:
            print(hero)


def update_heroes(engine):
    with Session(engine) as session:
        statement = select(Hero).where(Hero.name == "Spider-Boy")
        hero = session.exec(statement).first()
        print("Hero:", hero)

        hero.age = 16
        session.add(hero)
        session.commit()
        session.refresh(hero)
        print("Updated hero:", hero)


def delete_heroes(engine):
    with Session(engine) as session:
        statement = select(Hero).where(Hero.name == "Spider-Youngster")
        hero = session.exec(statement).first()
        print("Hero: ", hero)
        if not hero:
            return
        session.delete(hero)
        session.commit()
        print("Deleted hero:", hero)

        # statement = select(Hero).where(Hero.name == "Spider-Youngster")
        # results = session.exec(statement)
        # hero = results.first()
        # if hero is None:
        #     print("There's no hero named Spider-Youngster")


def main():
    engine = create_engine("sqlite:///../data/database.db", echo=True)
    create_db_and_tables(engine)
    # insert_heroes(engine)
    # select_heroes(engine)
    # update_heroes(engine)
    # delete_heroes(engine)


if __name__ == '__main__':
    main()
