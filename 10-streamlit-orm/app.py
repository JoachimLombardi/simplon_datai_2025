# import basics
import os
import pandas as pd
from os.path import join
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.model import Names, Firstnames, Hair_colors, Genres, Students, Base
from sqlalchemy_utils import database_exists, create_database, drop_database
import config

# Importation des informations de connexion
DATABASE_HOST = config.DATABASE_HOST
DATABASE_NAME = config.DATABASE_NAME
DATABASE_USERNAME = config.DATABASE_USERNAME
DATABASE_PASSWORD = config.DATABASE_PASSWORD
DATABASE_PORT = config.DATABASE_PORT

# Création du moteur de base de données
engine = create_engine(f"mysql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}")

# Création de la connexion à la base de données
# engine = create_engine("mysql+pymysql://root:root@localhost/my_database_tmp")
if database_exists(engine.url):
    drop_database(engine.url)    

create_database(engine.url)
print("is database existing?: ", database_exists(engine.url))

# Création des tables
Base.metadata.create_all(engine)

# Création d'une session
Session = sessionmaker(bind=engine)
session = Session()

# Création de liste d'élement à insérer

names = [
    Names(name="Dupont"),
    Names(name= "Durand"),
    Names(name="Martin"),
    Names(name="Lefebvre")
]
session.add_all(names)
session.commit()

firstnames = [
    Firstnames(firstname="Marie"),
    Firstnames(firstname="Jean"),
    Firstnames(firstname="Paul"),
    Firstnames(firstname="Jacques"),
    Firstnames(firstname="Pierre"),
    Firstnames(firstname="Antoine"),
]
session.add_all(firstnames)
session.commit()

hair_colors = [
    Hair_colors(hair_color="Blond"),
    Hair_colors(hair_color="Brun"),
    Hair_colors(hair_color="Roux"),
    Hair_colors(hair_color="Noir"),
    Hair_colors(hair_color="Marron")
]
session.add_all(hair_colors)
session.commit()

genres = [
    Genres(genre="Femme"),
    Genres(genre="Homme")
]
session.add_all(genres)
session.commit()

students = [
    Students(name_id=1, 
             firstname_id=3, 
             age=20, 
             email="1@1.com", 
             phone="0616560646", 
             poids=50, 
             hair_color_id=5, 
             genre_id=1),
    Students(name_id=2,
             firstname_id=4,
             age=22,
             email="2@2.com",
             phone="0657062406",
             poids=60,
             hair_color_id=1,
             genre_id=2),
    Students(name_id=2,
             firstname_id=6,
             age=24,
             email="6@6.com",
             phone="0657052416",
             poids=90,
             hair_color_id=4,
             genre_id=2),
    Students(name_id=1,
             firstname_id=6,
             age=26,
             email="7@7.com",
             phone="0657052416",
             poids=80,
             hair_color_id=2,
             genre_id=2),
    Students(name_id=3,
             firstname_id=2,
             age=28,
             email="8@8.com",
             phone="0657159416",
             poids=70,
             hair_color_id=3,
             genre_id=1),
    Students(name_id=2,
             firstname_id=2,
             age=30,
             email="9@9.com",
             phone="0651052416",
             poids=100,
             hair_color_id=5,
             genre_id=2),
    Students(name_id=3,
             firstname_id=1,
             age=23,
             email="10@10.com",
             phone="0645123698",
             poids=60,
             hair_color_id=4,
             genre_id=2)            
]
session.add_all(students)
session.commit()
session.close()

def add_user(name, firstname, age, email, phone, poids, couleur_de_cheveux, genre):

    Session = sessionmaker(bind=engine)
    session = Session()

    names_exist = session.query(Names).filter(Names.name == name).count()
    if names_exist == 0:
        names = Names(name=name)
        session.add(names)
        session.commit()
    else:
        names.id = session.query(Names).filter(Names.name == name).first().id

    
    firstnames_exist = session.query(Firstnames).filter(Firstnames.firstname == firstname).count()
    if firstnames_exist == 0:
        firstnames = Firstnames(firstname=firstname)
        session.add(firstnames)
        session.commit()
    else:
        firstnames.id = session.query(Firstnames).filter(Firstnames.firstname == firstname).first().id

    hair_colors_exist = session.query(Hair_colors).filter(Hair_colors.hair_color == couleur_de_cheveux).count()
    if hair_colors_exist == 0:
        hair_colors = Hair_colors(hair_color=couleur_de_cheveux)
        session.add(hair_colors)
        session.commit()
    else:
        hair_colors.id = session.query(Hair_colors).filter(Hair_colors.hair_color == couleur_de_cheveux).first().id

    genres_exist = session.query(Genres).filter(Genres.genre == genre).count()
    if genres_exist == 0:
        genres = Genres(genre=genre)
        session.add(genres)
        session.commit()
    else:
        genres.id = session.query(Genres).filter(Genres.genre == genre).first().id

    students = Students(name_id=names.id, firstname_id=firstnames.id, age=age, email=email, phone=phone, poids=poids, hair_color_id=hair_colors.id, genre_id=genres.id)
    session.add(students)
    session.commit()

    session.close()

def user_exist(name, firstname):
    session = sessionmaker(bind=engine)
    session = session()

    name_exist = session.query(Names).filter(Names.name == name).count()
    if name_exist == 0:
        return False

    firstname_exist = session.query(Firstnames).filter(Firstnames.firstname == firstname).count()
    if firstname_exist == 0:
        return False
    
    name_id = session.query(Names).filter(Names.name == name).first().id
    firstname_id = session.query(Firstnames).filter(Firstnames.firstname == firstname).first().id
    student_exist = session.query(Students).filter(Students.name_id == name_id and Students.firstname_id == firstname_id).count()
    if student_exist == 0:
        return False
    
    return True

def change_user(name, firstname, new_name, new_firstname, age, email, phone, poids,  new_couleur_de_cheveux, new_genre):

    Session = sessionmaker(bind=engine)
    session = Session()

    name_id = session.query(Names).filter(Names.name == name).first().id
    firstname_id = session.query(Firstnames).filter(Firstnames.firstname == firstname).first().id
    students = session.query(Students).filter(Students.name_id == name_id and Students.firstname_id == firstname_id).first()

    new_name_exist = session.query(Names).filter(Names.name == new_name).count()
    if new_name_exist == 0:
        new_names = Names(name=new_name)
        session.add(new_names)
        session.commit()
    else:
        students.name_id = session.query(Names).filter(Names.name == new_name).first().id

    new_firstname_exist = session.query(Firstnames).filter(Firstnames.firstname == new_firstname).count()
    if new_firstname_exist == 0:
        new_firstnames = Firstnames(firstname=new_firstname)
        session.add(new_firstnames)
        session.commit()
    else:
        students.firstname_id = session.query(Firstnames).filter(Firstnames.firstname == new_firstname).first().id

    new_couleur_de_cheveux_exist = session.query(Hair_colors).filter(Hair_colors.hair_color == new_couleur_de_cheveux).count()
    if new_couleur_de_cheveux_exist == 0:
        new_hair_colors = Hair_colors(hair_color=new_couleur_de_cheveux)
        session.add(new_hair_colors)
        session.commit()
    else:
        students.hair_color_id = session.query(Hair_colors).filter(Hair_colors.hair_color == new_couleur_de_cheveux).first().id

    new_genre_exist = session.query(Genres).filter(Genres.genre == new_genre).count()
    if new_genre_exist == 0:
        new_genres = Genres(genre=new_genre)
        session.add(new_genres)
        session.commit()
    else:
        students.genre_id = session.query(Genres).filter(Genres.genre == new_genre).first().id

    students.age = age
    students.email = email
    students.phone = phone
    students.poids = poids

    session.commit()

    session.close()