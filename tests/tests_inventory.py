import unittest
from inventory import InventoryManager

class TestInventoryManager(unittest.TestCase):
    """Testes pour la gestion des produits dans l'inventaire"""

    def setUp(self):
        """Préparer un inventaire pour les tests"""
        self.manager = InventoryManager()

    def test_search_product_found(self):
        """Tester la recherche d'un produit existant"""
        # Simuler le chargement d'un fichier CSV avec des produits
        self.manager.load_csv('tests/test_products.csv')
        results = self.manager.search_product('Product A')
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]['name'], 'Product A')

    def test_search_product_not_found(self):
        """Tester la recherche d'un produit inexistant"""
        self.manager.load_csv('tests/test_products.csv')
        results = self.manager.search_product('NonExistentProduct')
        self.assertEqual(len(results), 0)

if __name__ == "__main__":
    unittest.main()
