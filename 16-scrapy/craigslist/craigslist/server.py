from pymongo import MongoClient
from flask import Flask, request
import json

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client.gpt_db
collection = db.quotes

# Rechercher par index
@app.route("/search", methods=["GET"])
def search():
    try:
        query = request.args.get('query')
        results = collection.find({"$text": {"$search": query}}) # $text exploite l'index texte
        liste = list(results) 
        new_liste = []
        for result in liste:
            new_liste.append({"quote": result["quote"], "author": result["author"]})
        return json.dumps(new_liste)
    except Exception as e:
        return json.dumps({"error": str(e)})

# Choisir une citation au hasard dans mong db
@app.route("/random", methods=["GET"])
def random():
    try:
        quote_number = int(request.args.get('number'))
        results = collection.aggregate([{"$sample": {"size": quote_number}}]) # Selectionne une citation au hasard, $sample permet de selectionner une citation au hasard
        liste = list(results)
        new_liste = []
        for result in liste:
            new_liste.append({"quote": result["quote"], "author": result["author"]})
        return json.dumps(new_liste)
    except Exception as e:
        return json.dumps({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True) 