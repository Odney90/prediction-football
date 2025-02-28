import requests
import pandas as pd
import os

# Configuration de l'API
API_USER = "lundiodney"
API_TOKEN = "623654d91c81ceed9379be5968f089d8"
BASE_URL = "https://api.soccersapi.com/v2.2/leagues/"
PARAMS = {"user": API_USER, "token": API_TOKEN, "t": "list"}

# Vérification du dossier de stockage
DATA_PATH = "data"
FILE_PATH = os.path.join(DATA_PATH, "matchs.csv")
if not os.path.exists(DATA_PATH):
    os.makedirs(DATA_PATH)

# Récupération des données de ligues
response = requests.get(BASE_URL, params=PARAMS)
data = response.json()

leagues_stats = []
if "data" in data:
    for league in data["data"]:
        leagues_stats.append({
            "Ligue": league["name"],
            "Pays": league["country"],
            "Saison": league["season"],
            "Type": league["type"],
            "BSVM": league.get("bsvm", "N/A")  # Ajout de la valeur BSVN si disponible
        })

# Convertir en DataFrame
leagues_df = pd.DataFrame(leagues_stats)

# Sauvegarde en CSV
leagues_df.to_csv(FILE_PATH, index=False)

print("✅ Données récupérées et enregistrées dans", FILE_PATH)
