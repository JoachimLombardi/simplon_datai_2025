import json
from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)
app.testing = True
app.config.update(
    TEMPLATES_AUTO_RELOAD = True
)


@app.route("/products", methods=["GET"])
def get_products():
    products = [
    {"name": "Product 1","price": 100},
    {"name": "Product 2","price": 200}]
    response = json.dumps(products)
    return response, 200

# @app.route('/user/<username>', methods=['GET'])
# def show_user_profile(username):
#     # show the user profile for that user
#     return json.dumps(f'User {escape(username)}')

if __name__ == "__main__": # pour lancer le serveur python avec flask c'est le port 5000
    app.run(port=8080)