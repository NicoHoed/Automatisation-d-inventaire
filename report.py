import csv
from typing import List, Dict


def generate_report(products: Dict) -> None:
    """
    Génère un rapport récapitulatif de l'inventaire.

    Args:
        products (dict): Dictionnaire des produits par catégorie.
    """
    with open('inventory_report.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Category", "Product Name", "Quantity", "Price"])
        for category, items in products.items():
            for item in items:
                writer.writerow([category, item['name'], item['quantity'], item['price']])
    print("Le rapport a été généré avec succès : inventory_report.csv")
