import streamlit as st
import numpy as np
from matplotlib import pyplot as plt
# import sounddevice as sd
import seaborn as sns
import pandas as pd
from pymongo import MongoClient, errors
import sqlite3
import mysql.connector
import plotly.express as px



st.title("Tableau de Bord Simple")
st.write("voici ma première application Streamlit.")
if st.button("Cliquez ici !"):
    st.write("Vous avez cliqué sur le bouton ci-dessus.")
age = st.slider("Veuillez indiquer votre âge", 0, 100, 25)
st.write("Vous avez", age, "ans")
st.write("Veuillez entrer votre nom")
nom = st.text_input("Nom")
if (nom):
    st.write("Bonjour", nom)
if st.checkbox("J'accepte les termes d'utilisation"):
    st.write("Vous avez accepté les termes d'utilisation.")

t = np.linspace(0, 1)
freq = st.slider("Fréquence",0, 100, 1) 
y = np.sin(2 * np.pi * freq * t)
st.line_chart(y)

# def sinusoids(a,f,Fs,T,phase):

#     t = np.arange(0,Fs*T) # pour une seconde
#     s = 0 
#     for i,freq in enumerate(f):

#         s += a[i] * np.sin(2*np.pi*freq*t/Fs + 2*np.pi/360*phase[i])
#     return s

# N = 1
# a = np.random.rand(N)
# f = np.random.rand(N)*256
# phase = np.random.randn(N)*360
# Fs = 44100 
# T = 2

# a[0] = 1
# f[0] = 440

# x = sinusoids(a,f,Fs,T,phase)

# x = x/np.abs(x).max() 
# sd.play(x,Fs)

button_html = """
<style>
    .stButton>button {
        background-color: green;
        color: white;
        border: 2px solid black;
        border-radius: 8px;
    }
</style>
"""

st.markdown(button_html, unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["Graphique à barres", "Graphique circulaire", "Page 3"])

categorie = ["Chien", "Chat", "Souris"]
nombre = [1, 2, 3]

# Créer le graphique
fig, ax = plt.subplots()

tab1, tab2, tab3 = st.tabs(["Graphique à Barres", "Graphique circulaire", "Graphique à Arcs"])

categorie = ["Femme", "Homme"]
nombre = [20, 30]


# sns.barplot(x=categorie, y=nombre)

with tab1:
    st.header("Graphique à Barres interactif")
    fig1, ax1 = plt.subplots(figsize=(10, 7))
    plt.ion()
    plt.isinteractive()
    plt.bar(x=categorie, height=nombre)
   # st.bar_chart(dict(zip(categorie, nombre)))
    st.pyplot(fig1)

with tab2:
    st.header("Graphique circulaire interactif")
    data_circ = dict(
    character=["Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"],
    parent=["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve" ],
    value=[10, 14, 12, 10, 2, 6, 6, 4, 4])

    fig = px.sunburst(data_circ,
                      names='character',
                      parents='parent',
                      values='value')
    st.plotly_chart(fig)

with tab3:
    st.header("Graphique à Arcs")
    st.line_chart()

st.sidebar.title("Lecture et Affichage de Données depuis Différents Fichiers")

# Choix du fichier
choice = st.sidebar.selectbox("Fichier", ["Fichier CSV", "Fichier Excel", "Fichier JSON"])

# Lire les données du fichier CSV
if choice == "Fichier CSV":
    st.write("Lecture de données depuis un fichier CSV")
    fichier_csv = st.file_uploader("fichier csv", type=["csv"]) 
    if fichier_csv is not None:
        df = pd.read_csv(fichier_csv)
        st.dataframe(df)

# Lire les données du fichier Excel
elif choice == "Fichier Excel":
    st.write("Lecture de données depuis un fichier Excel")
    fichier_excel = st.file_uploader("fichier excel", type=["xlsx", "xls"]) 
    if fichier_excel is not None:
        df = pd.read_csv(fichier_excel)
        st.dataframe(df)

# Lire les données du fichier JSON
elif choice == "Fichier JSON":
    st.write("Lecture de données depuis un fichier JSON")
    fichier_json = st.file_uploader("Fichier json", type=["json"]) 
    if fichier_json is not None:
        df = pd.read_json(fichier_json)
        st.dataframe(df)
    if fichier_json is not None:
        df = pd.read_csv(fichier_json)
        st.dataframe(df)


st.title("Connexion à une Base de Données NoSQL (MongoDB)")
client = MongoClient("mongodb://localhost:27017/")
db = client["ma_base_de_données"]
collection = db["utilisateurs"]

nom_utilisateur = st.empty()
email_utilisateur = st.empty()

st.subheader("Ajouter un utilisateur")
nom_utilisateur = st.text_input("Ajoutez un utilisateur avec un nom")
email_utilisateur = st.text_input("Ajoutez un utilisateur un email")
if st.button("Ajouter"):
    if nom_utilisateur and email_utilisateur:
        try:
            nouvel_utilisateur = {"nom": nom_utilisateur, "email": email_utilisateur}
            collection.insert_one(nouvel_utilisateur)
            st.success("L'utilisateur a bien été ajouté")
        except errors.DuplicateKeyError:
            st.error(f"L'utilisateur {email_utilisateur} existe déjà.")
    else:
        st.error("Veuillez entrer un nom et un email")

st.subheader("Utilisateurs Existants")
utilisateurs = collection.find()
for utilisateur in utilisateurs:
    st.markdown(f"Nom: {utilisateur['nom']}<br>Email: {utilisateur['email']}", unsafe_allow_html=True)

client.close()

# Créez une connexion au serveur MySQL

st.title("Connexion à une Base de Données SQL (MySql/MariaDb)")
# Remplacez les valeurs suivantes par les informations de connexion à votre serveur MySQL
host = "localhost" # L'hôte du serveur MySQL
user = "root"  # Votre nom d'utilisateur MySQL
password = "root"  # Votre mot de passe MySQL
database_name = "ma_bdd_streamlit"
port = "3307"

# Créez une connexion au serveur MySQL
conn = mysql.connector.connect(
    host=host,
    user=user,
    port = port,
    password=password
)

cursor = conn.cursor()

# Exécutez une requête SQL pour obtenir la liste des bases de données
cursor.execute("SHOW DATABASES")

databases = cursor.fetchall()
database_name = "ma_bdd_streamlit"

# Vérifiez si la base de données que vous recherchez existe
if (database_name,) in databases:
    print(f"La base de données '{database_name}' existe.")
else:
    print(f"La base de données '{database_name}' n'existe pas.")
     # Utilisez le curseur pour exécuter une commande SQL de création de base de données
    create_database_query = f"CREATE DATABASE {database_name}"
    cursor.execute(create_database_query)
    print(f"La base de données '{database_name}' a été créée avec succès.")

cursor.close()
conn.close()

# Créez une connexion à la base de données
conn = mysql.connector.connect(
    host=host,
    user=user,
    port = port,
    password=password,
    database=database_name
)

cursor = conn.cursor()

# Utilisez le curseur pour exécuter une requête SQL pour obtenir la liste des tables de la base de données
cursor.execute("SHOW TABLES")

tables = cursor.fetchall()

table_name = "utilisateurs"

if (f"{table_name}",) in tables:
    print(f"La table '{table_name}' existe.")
else:
    print(f"La table '{table_name}' n'existe pas.")
    # Définissez la commande SQL pour créer une table
    create_table_utilisateurs = f"""
    CREATE TABLE {table_name} (
        id SMALLINT AUTO_INCREMENT PRIMARY KEY,
        nom VARCHAR(255),
        email VARCHAR(255) 
    )
    """
    # Exécutez la commande SQL pour créer la table
    cursor.execute(create_table_utilisateurs)

    # Validez la création de la table
    conn.commit()

    print(f"La table '{table_name}' a été créée avec succès.")

# Formulaire pour ajouter un utilisateur
st.header("Ajouter un utilisateur")
nom_utilisateur = st.text_input("Ajoutez un utilisateur avec un nom", key=1)
email_utilisateur = st.text_input("Ajoutez un utilisateur un email", key=2)
if st.button("Ajouter", key=3):
    if nom_utilisateur and email_utilisateur:
       insert_query = f"""INSERT INTO {table_name} (nom, email) VALUES ('{nom_utilisateur}', '{email_utilisateur}')"""
       cursor.execute(insert_query)
       conn.commit() 
       st.success(f"L'utilisateur {nom_utilisateur} a bien été ajouté")
    else:
        st.error("Veuillez entrer un nom et un email")

# Affichez les utilisateurs existants
st.header("Utilisateurs")
cursor.execute(f"SELECT * FROM {table_name}")
utilisateurs = cursor.fetchall()
for utilisateur in utilisateurs:
    st.markdown(f"Nom: {utilisateur[1]}<br>Email: {utilisateur[2]}", unsafe_allow_html=True)

# Fermez le curseur et la connexion
cursor.close()
conn.close()









