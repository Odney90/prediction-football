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

        matches = []
        for league in data['data']:
            matches.append({
                "league_id": league["id"],
                "league_name": league["name"],
                "country": league["country"],
                "season": league["season"],
            })

        df = pd.DataFrame(matches)
        os.makedirs("../data", exist_ok=True)
        df.to_csv(DATA_PATH, index=False)
        print("✅ Données récupérées et enregistrées avec succès !")
    
    except requests.exceptions.RequestException as e:
        print(f"❌ Erreur lors de la récupération des données : {e}")
        handle_manual_entry()


def handle_manual_entry():
    print("📝 Saisie manuelle des données...")
    matches = []
    while True:
        league_id = input("ID de la ligue : ")
        league_name = input("Nom de la ligue : ")
        country = input("Pays : ")
        season = input("Saison : ")

        matches.append({
            "league_id": league_id,
            "league_name": league_name,
            "country": country,
            "season": season,
        })
        
        cont = input("Ajouter une autre ligue ? (o/n) : ")
        if cont.lower() != 'o':
            break
    
    df = pd.DataFrame(matches)
    os.makedirs("../data", exist_ok=True)
    df.to_csv(DATA_PATH, index=False, mode='a', header=not os.path.exists(DATA_PATH))
    print("✅ Données ajoutées manuellement et enregistrées !")

if __name__ == "__main__":
    fetch_data()

