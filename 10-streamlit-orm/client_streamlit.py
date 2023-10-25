import streamlit as st
import numpy as np
from matplotlib import pyplot as plt
# import sounddevice as sd
import seaborn as sns
import pandas as pd
from app import add_user, change_user, user_exist


st.title("Connexion à une Base de Données SQL (MySql/MariaDb)")

# Formulaire pour ajouter un utilisateur
st.header("Ajouter un utilisateur")

# Formulaire pour ajouter un utilisateur
nom_utilisateur = st.text_input("Entrez un nom", key=1)
prenom_utilisateur = st.text_input("Entrez un prénom", key=2)
age_utilisateur = st.text_input("Entrez un age", key=3)
email_utilisateur = st.text_input("Entrez un email", key=4)
telephone_utilisateur = st.text_input("Entrez un numéro de téléphone", key=5)
poids_utilisateur = st.text_input("Entrez un poids", key=6)
couleur_de_cheveux = st.text_input("Entrez une couleur de cheveux", key=7)
genre_utilisateur = st.text_input("Entrez un genre", key=8)

if st.button("Ajouter"):
    if nom_utilisateur and prenom_utilisateur and age_utilisateur and email_utilisateur and telephone_utilisateur and poids_utilisateur and couleur_de_cheveux and genre_utilisateur:
       add_user(nom_utilisateur, prenom_utilisateur, age_utilisateur, email_utilisateur, telephone_utilisateur, poids_utilisateur, couleur_de_cheveux, genre_utilisateur) 
       st.success("L'utilisateur a bien été ajouté")
    else:
      st.error("Veuillez remplir tous les champs")

# Formulaire pour modifier un utilisateur
nom_utilisateur_exist = st.text_input("Entrez un nom", key=9)
prenom_utilisateur_exist = st.text_input("Entrez un prénom", key=10)

if st.button("Modifier"):
    if nom_utilisateur_exist and prenom_utilisateur_exist:
        if user_exist(nom_utilisateur_exist, prenom_utilisateur_exist):
            nom_utilisateur_mod = st.text_input("Entrez un nouveau nom", key=11)
            prenom_utilisateur_mod = st.text_input("Entrez un nouveau prénom", key=12)
            age_utilisateur_mod = st.text_input("Entrez un nouveau age", key=13)
            email_utilisateur_mod = st.text_input("Entrez un nouveau email", key=14)
            telephone_utilisateur_mod = st.text_input("Entrez un nouveau numéro de téléphone", key=15)
            poids_utilisateur_mod = st.text_input("Entrez un nouveau poids", key=16)
            couleur_de_cheveux_mod = st.text_input("Entrez une nouvelle couleur de cheveux", key=17)
            genre_utilisateur_mod = st.text_input("Entrez un nouveau genre", key=18)
            if st.button("Valider", key=19):
                change_user(nom_utilisateur_exist, prenom_utilisateur_exist, nom_utilisateur_mod, prenom_utilisateur_mod, age_utilisateur_mod, email_utilisateur_mod, telephone_utilisateur_mod, poids_utilisateur_mod, couleur_de_cheveux_mod, genre_utilisateur_mod)
                st.success("L'utilisateur a bien été modifié")
        else:
            st.error("L'utilisateur n'existe pas")
    else:
        st.error("Veuillez remplir tous les champs")