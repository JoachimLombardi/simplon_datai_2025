from flask import Flask, render_template, jsonify, json
import mysql
from pathlib import Path
import pandas as pd

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])

def get_data():
    bikes_data_path = Path() / 'api/data/student_grades.csv'
    data = pd.read_csv(bikes_data_path)
    return json.dumps(data.to_json())

def index():
    # Créez une connexion au serveur MySQL
    # Remplacez les valeurs suivantes par les informations de connexion à votre serveur MySQL
    host = "localhost" # L'hôte du serveur MySQL
    user = "root"  # Votre nom d'utilisateur MySQL
    password = "root"  # Votre mot de passe MySQL
    database_name = "ma_bdd_streamlit"
    port = "3307"

    # Créez une connexion à la base de données
    conn = mysql.connector.connect(
    host=host,
    user=user,
    port = port,
    password=password,
    database=database_name)

    utilisateurs = conn.execute('SELECT * FROM utilisateurs').fetchall()
    conn.close()

    #Exécutez l'application Streamlit en arrière-plan
    #subprocess.Popen(["streamlit", "run", "streamlit_client.py"])
    return render_template('index.html',
                           name="jojo",
                           utilisateurs=utilisateurs)

if __name__ == '__main__':
    app.run(debug=True)