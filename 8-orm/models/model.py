# Importez les modules SQLAlchemy et définissez votre modèle de base
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Créez une classe Employee record
class Products(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    price = Column(Float())

class Customers(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    email = Column(String(255))

class Orders(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id')) #ondelete='CASCADE' permet de supprimer la ligne où que soit réalisée la supression
    customer = relationship(Customers)#, backref='orders', cascade='all, delete-orphan', single_parent=True)
    product_id = Column(Integer, ForeignKey('products.id')) #ondelete='CASCADE'
    product = relationship(Products)#, backref='orders', cascade='all, delete-orphan', single_parent=True)