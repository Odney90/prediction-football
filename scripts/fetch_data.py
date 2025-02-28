import requests
import pandas as pd
import os

# Définition des paramètres de l'API
API_URL = "https://api.soccersapi.com/v2.2/leagues/?user=lundiodney&token=623654d91c81ceed9379be5968f089d8&t=list"

# Chemin du fichier de stockage
DATA_PATH = "../data/matchs.csv"  # Remonte d'un niveau vers le dossier data

def fetch_data():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        data = response.json()

        # ➜ Afficher toute la réponse de l'API
        print("🔹 Réponse complète de l'API :")
        print(data)

        # ➜ Afficher un exemple de ligue
        if "data" in data and len(data["data"]) > 0:
            print("🔹 Exemple de structure d'une ligue :")
            print(data["data"][0])
    
    except requests.exceptions.RequestException as e:
        print(f"❌ Erreur lors de la récupération des données : {e}")

fetch_data()
