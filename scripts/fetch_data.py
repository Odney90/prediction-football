import requests
import pandas as pd
import os

# Définition des paramètres de l'API
API_URL = "https://api.soccersapi.com/v2.2/leagues/?user=lundiodney&token=623654d91c81ceed9379be5968f089d8&t=list"

# Chemin du fichier de stockage
DATA_DIR = "../data"
DATA_PATH = os.path.join(DATA_DIR, "matchs.csv")  # Chemin absolu

def fetch_data():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        data = response.json()

        if "data" not in data or not isinstance(data["data"], list):
            print("❌ Erreur: La réponse de l'API ne contient pas de données valides.")
            return

        matches = []
        for league in data['data']:
            match_info = {
                "league_id": league.get("id", "N/A"),
                "league_name": league.get("name", "N/A"),
                "country": league.get("country_name", "N/A"),
                "season": league.get("current_season_id", "N/A"),
            }
            matches.append(match_info)

        # Vérification des données avant enregistrement
        print(f"🔹 Nombre total d'éléments dans matches : {len(matches)}")
        if not matches:
            print("❌ Aucune donnée récupérée !")
            return

        # Création du DataFrame
        df = pd.DataFrame(matches)
        print("🔹 Aperçu du DataFrame avant l'enregistrement :")
        print(df.head())

        # Vérifier et créer le dossier data
        os.makedirs(DATA_DIR, exist_ok=True)

        # Forcer l'écriture et l'affichage du fichier
        df.to_csv(DATA_PATH, index=False)
        print(f"✅ Données enregistrées dans {DATA_PATH}")

        # Vérification immédiate du fichier
        print("🔹 Vérification du contenu du fichier après écriture :")
        with open(DATA_PATH, "r") as f:
            content = f.read()
            print(content)

    except requests.exceptions.RequestException as e:
        print(f"❌ Erreur lors de la récupération des données : {e}")

if __name__ == "__main__":
    fetch_data()
