import argparse
from inventory import InventoryManager
from report import generate_report


def main():
    parser = argparse.ArgumentParser(description="Gestion des stocks de l'entreprise.")
    parser.add_argument('--load', help="Charger un fichier CSV d'inventaire", type=str)
    parser.add_argument('--search', help="Rechercher un produit par nom", type=str)
    parser.add_argument('--report', help="Générer un rapport récapitulatif", action='store_true')

    args = parser.parse_args()

    manager = InventoryManager()

    if args.load:
        manager.load_csv(args.load)

    if args.search:
        results = manager.search_product(args.search)
        if results:
            for product in results:
                print(product)
        else:
            print(f"Aucun produit trouvé pour '{args.search}'.")

    if args.report:
        generate_report(manager.products)


if __name__ == "__main__":
    main()
