import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

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
    student_grades = st.file_uploader("student_grades.csv") 
    if student_grades is not None:
        df = pd.read_csv(student_grades)
        st.dataframe(df)
elif choice == "Fichier Excel":
    st.write("Lecture de données depuis un fichier Excel")
elif choice == "Fichier JSON":
    st.write("Lecture de données depuis un fichier JSON")


