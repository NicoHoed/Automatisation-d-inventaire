import unittest
import os
from report import generate_report
from inventory import InventoryManager

class TestReportGeneration(unittest.TestCase):
    """Test pour la génération du rapport d'inventaire"""

    def setUp(self):
        """Préparer les données pour les tests"""
        self.manager = InventoryManager()
        # Ajouter des produits manuellement pour le test
        self.manager.products['category1'] = [
            {'name': 'Product A', 'quantity': 10, 'price': 15.0, 'category': 'category1'},
            {'name': 'Product B', 'quantity': 5, 'price': 20.0, 'category': 'category1'}
        ]

    def test_generate_report(self):
        """Tester la génération du rapport CSV"""
        generate_report(self.manager.products)
        # Vérifier si le fichier report a bien été créé
        self.assertTrue(os.path.exists('inventory_report.csv'))

    def tearDown(self):
        """Nettoyer après les tests"""
        if os.path.exists('inventory_report.csv'):
            os.remove('inventory_report.csv')

if __name__ == "__main__":
    unittest.main()
