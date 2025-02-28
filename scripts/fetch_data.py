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

        # Vérification de la récupération des données
        print("🔹 Vérification après la boucle :")
        print(f"Nombre total d'éléments dans matches : {len(matches)}")
        print("🔹 Contenu de matches :", matches)
        
        if not matches:
            print("❌ Aucune donnée récupérée !")
            return

        # Création du DataFrame
        df = pd.DataFrame(matches)
        print("🔹 Contenu du DataFrame avant l'enregistrement :")
        print(df.to_string())  # Affichage complet

        # Vérifier si le dossier data existe avant d'écrire
        os.makedirs("../data", exist_ok=True)
        df.to_csv(DATA_PATH, index=False)
        print("✅ Données enregistrées dans matchs.csv !")
    
    except requests.exceptions.RequestException as e:
        print(f"❌ Erreur lors de la récupération des données : {e}")

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
print("🔹 Vérification finale avant création du DataFrame :")
print(f"Nombre total d'éléments dans matches : {len(matches)}")
print("🔹 Contenu de matches :", matches)

    df = pd.DataFrame(matches)
    os.makedirs("../data", exist_ok=True)
    df.to_csv(DATA_PATH, index=False, mode='a', header=not os.path.exists(DATA_PATH))
    print("✅ Données ajoutées manuellement et enregistrées !")

if __name__ == "__main__":
    fetch_data()
