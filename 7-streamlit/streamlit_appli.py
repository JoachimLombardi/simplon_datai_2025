import streamlit as st
import numpy as np
from matplotlib import pyplot as plt
import mplcursors as mpc


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

import sounddevice as sd
import numpy as np 

def sinusoids(a,f,Fs,T,phase):

    t = np.arange(0,Fs*T) # pour une seconde
    s = 0 
    for i,freq in enumerate(f):

        s += a[i] * np.sin(2*np.pi*freq*t/Fs + 2*np.pi/360*phase[i])
    return s

N = 1
a = np.random.rand(N)
f = np.random.rand(N)*256
phase = np.random.randn(N)*360
Fs = 44100 
T = 2

a[0] = 1
f[0] = 440

x = sinusoids(a,f,Fs,T,phase)

x = x/np.abs(x).max() 
sd.play(x,Fs)



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
ax.bar(x, y)
ax.set_xticks(x)
ax.set_xticklabels(nombre)

# Ajouter des curseurs interactifs
cursor = mpc.cursor(hover=True)
cursor.connect("add", lambda sel: sel.annotation.set_text(f'Valeur: {sel.artist.get_height()}'))

# Afficher le graphique interactif
plt.show()

# Créer un onglet "Page 1"
with  tab1:
    st.title("Graphique à barres interactif")
    st.write("Contenu de la page 1")
    st.pyplot(fig)

# Créer un onglet "Page 2"
with tab2:
    st.title("Graphique circulaire interactif")
    st.write("Contenu de la page 2")

# Créer un onglet "Page 3"
with tab3:
    st.title("Code")
    st.write("Contenu de la page 3")


