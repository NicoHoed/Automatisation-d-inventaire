import csv
from typing import List, Dict


def read_csv(file_path: str) -> List[Dict]:
    """
    Lit un fichier CSV et retourne une liste de dictionnaires représentant les produits.

    Args:
        file_path (str): Le chemin vers le fichier CSV.

    Returns:
        List[Dict]: Une liste de dictionnaires représentant les produits.
    """
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]
    except FileNotFoundError:
        print(f"Erreur : Le fichier {file_path} est introuvable.")
    except csv.Error as e:
        print(f"Erreur de lecture CSV : {e}")
