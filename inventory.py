import csv
from collections import defaultdict
from typing import List, Dict


class InventoryManager:
    """Classe responsable de la gestion de l'inventaire."""

    def __init__(self):
        """Initialise un gestionnaire d'inventaire vide."""
        self.products = defaultdict(list)

    def load_csv(self, file_path: str) -> None:
        """
        Charge un fichier CSV et met à jour l'inventaire.

        Args:
            file_path (str): Le chemin vers le fichier CSV à charger.
        """
        try:
            with open(file_path, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.products[row['category']].append(row)
        except FileNotFoundError:
            print(f"Erreur : Le fichier {file_path} est introuvable.")
        except csv.Error as e:
            print(f"Erreur de lecture CSV : {e}")

    def search_product(self, name: str) -> List[Dict]:
        """
        Recherche un produit par son nom dans l'inventaire.

        Args:
            name (str): Le nom du produit à rechercher.

        Returns:
            List[Dict]: Liste des produits correspondants.
        """
        results = []
        for category, items in self.products.items():
            for item in items:
                if name.lower() in item['name'].lower():
                    results.append(item)
        return results
