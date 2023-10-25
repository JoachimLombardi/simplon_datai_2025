# import basics
import os
import pandas as pd
from os.path import join
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload
from models.model import Products, Customers, Orders, Base
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

# Définir le nom de la base de données
def bk():
    return print("\n",79*'=','\n')

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

# Créations d'une liste de produits à insérer
products = [
    Products(name="produit 1", price=100),
    Products(name="produit 2", price=200)
]

# Insérer les données dans la base de données
session.add_all(products)
session.commit()
session.close()

# Création d'une session
Session = sessionmaker(bind=engine)
session = Session()

# Afficher les données de la base de données
products = session.query(Products).all()
for product in products:
    print(product.name,
          product.price)
session.close()

# Création d'une session
Session = sessionmaker(bind=engine)
session = Session()

# Remplissage des tables orders et customers
customers = [
    Customers(name="customer 1", email="email 1"),
    Customers(name="customer 2", email="email 2"),
]
session.add_all(customers)
session.commit()

customers = session.query(Customers).all()
orders = [
    Orders(customer_id=customers[0].id, product_id=products[0].id),
    Orders(customer_id=customers[1].id, product_id=products[1].id),
]
session.add_all(orders)
session.commit()
session.close()

# Création d'une session
Session = sessionmaker(bind=engine)
session = Session()

# Afficher les données de la base de données
orders = session.query(Orders).all()
products = session.query(Products).all()
customers = session.query(Customers).all()

for order in orders:
    print(order.customer_id,
          order.product_id)
    
for product in products:
    print(product.name,
          product.price)
    
for customer in customers:
    print(customer.name,
          customer.email)    

session.close()

# Création d'une session
Session = sessionmaker(bind=engine)
session = Session()

result = session.query(
    Products.name,
    Products.price,
    Customers.name,
    Customers.email
).join(Orders, Orders.product_id == Products.id ).join(Customers, Orders.customer_id == Customers.id).all()
    
for row in result:
    print(row)

session.close()

# Création d'une session
Session = sessionmaker(bind=engine)
session = Session()

# Mettre à jour le prix du produit 2
product_2 = session.query(Products).filter(Products.name == "produit 2").first()
product_2.price = 500
session.commit()
session.close()

# Création d'une session
Session = sessionmaker(bind=engine)
session = Session()

order_2 = session.query(Orders).options(joinedload(Orders.product), joinedload(Orders.customer)).filter(Orders.id == 2).first()
    
# Supprimer l'ordre 2

session.delete(order_2)
session.commit()
session.close()