import streamlit as st
from pymongo import MongoClient
import requests, json

client = MongoClient("mongodb://localhost:27017/")
db = client.gpt_db
collection = db.quotes

serveur_url = "http://localhost:5000"

def get_server_data():
    response = requests.get(f"{serveur_url}/search", params={"query": query})  
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error: ", response.status_code)

def random_quote():
    response = requests.get(f"{serveur_url}/random", params={"number": quote_number})
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error: ", response.status_code)

st.header("Citations")
st.write("Barre de recherche")
query = st.text_input("Veuillez entrer votre recherche")
if st.button("Recherche"):
    server_data = get_server_data()
    if server_data:
        for result in server_data:
            st.write(result["quote"], "- ", result["author"])
    else:
        st.write("Aucune citation")

st.write("Citation aleatoire")
quote_number = st.slider("Veuillez choisir un nombre de citations", 1, 5, 1)
if st.button("Citation aleatoire"): 
        data = random_quote()
        if data:
            for result in data:
                st.write(result["quote"], "- ", result["author"])
        else:
            st.write("Aucune citation")
