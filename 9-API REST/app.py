import requests

# URL de l'API
BASE_URL = "http://localhost:8080/products"

# Envoi de la requête
response = requests.get(BASE_URL, params={"name": "produit 2"})
# response = requests.get(BASE_URL, params={"username": "jojo"})

# Traitement de la réponse
if response.status_code == 200:
    res = response.json()

else:
    raise Exception(f"Erreur : {response.status_code}")

for product in res:
    print(product["name"], product["price"])

# Affichage des produits
# for product in products:
#     print(product["name"], product["price"])