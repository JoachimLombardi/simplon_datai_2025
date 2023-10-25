# Importez les modules SQLAlchemy et définissez votre modèle de base
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Names(Base):
    __tablename__ = 'names'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))

class Firstnames(Base):
    __tablename__ = 'firstnames'
    id = Column(Integer, primary_key=True)
    firstname = Column(String(255))

class Hair_colors(Base):
    __tablename__ = 'hair_colors'
    id = Column(Integer, primary_key=True)
    hair_color = Column(String(255))

class Genres(Base):
    __tablename__ = 'genres'
    id = Column(Integer, primary_key=True)
    genre = Column(String(255))

# Création d'une base étudiant
class Students(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name_id = Column(Integer, ForeignKey('names.id'))
    name = relationship(Names)
    firstname_id = Column(Integer, ForeignKey('firstnames.id'))
    firstname = relationship(Firstnames)
    age = Column(Integer)
    email = Column(String(255))
    phone = Column(String(255))
    poids = Column(Float)
    hair_color_id = Column(Integer, ForeignKey('hair_colors.id'))
    hair_color = relationship(Hair_colors)
    genre_id = Column(Integer, ForeignKey('genres.id'))
    genre = relationship(Genres)
    
