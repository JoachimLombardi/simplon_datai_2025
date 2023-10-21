import streamlit as st
import numpy as np
from matplotlib import pyplot as plt
# import sounddevice as sd
import seaborn as sns
import pandas as pd
from pymongo import MongoClient

st.title("Tableau de Bord Simple")
st.write("Je m'appelle Joachim, et voici ma première application Streamlit.")
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

categories = ['A', 'B', 'C', 'D']
valeurs = [30, 25, 15, 20]

fig1, ax1 = plt.subplots(figsize=(10, 7))
sns.barplot(x=categorie, y=nombre)

fig2, ax2 = plt.subplots(figsize=(10, 7))
ax2.pie(valeurs, 
        labels=categories, 
        explode = [0, 0.3, 0, 0], 
        colors=["gold", "yellow", "purple", "indigo"],
        shadow=True,
        labeldistance=0.8,
        autopct = lambda x: str(round(x, 2)) + '%',
        pctdistance = 0.4)
ax2.set(title="Camembert")

with tab1:
    st.header("Graphique à Barres interactif")
   # st.bar_chart(dict(zip(categorie, nombre)))
    st.pyplot(fig1)

with tab2:
    st.header("Graphique circulaire interactif")
    st.pyplot(fig2)

with tab3:
    st.header("Graphique à Arcs")
    st.line_chart()

st.sidebar.title("Lecture et Affichage de Données depuis Différents Fichiers")
choice = st.sidebar.selectbox("Fichier", ["Fichier CSV", "Fichier Excel", "Fichier JSON"])
if choice == "Fichier CSV":
    st.write("Lecture de données depuis un fichier CSV")
    placeholder = st.empty()
    student_grades = st.file_uploader("student_grades.csv") 
    if student_grades is not None:
        df = pd.read_csv(student_grades)
        placeholder.dataframe(df)
elif choice == "Fichier Excel":
    st.write("Lecture de données depuis un fichier Excel")
elif choice == "Fichier JSON":
    st.write("Lecture de données depuis un fichier JSON")

st.title("Connexion à une Base de Données NoSQL (MongoDB)")
client = MongoClient("mongodb://localhost:27017/")
db = client["ma_base_de_données"]
collection = db["utilisateurs"]
nom_utilisateur = st.text_input("Ajoutez un utilisateur avec un nom")
email_utilisateur = st.text_input("Ajoutez un utilisateur un email")
if st.button("Ajouter"):
    utilisateur = {"nom": nom_utilisateur, "email": email_utilisateur}
    collection.insert_one(utilisateur)
    st.success("L'utilisateur a bien été ajouté")