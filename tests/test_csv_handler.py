import unittest
from csv_handler import read_csv

class TestCSVHandler(unittest.TestCase):
    """tests pour la gestion des fichiers CSV"""

    def test_read_csv_valid(self):
        """Tester la lecture d'un fichier CSV valide"""
        products = read_csv('tests/test_products.csv')
        self.assertGreater(len(products), 0)
        self.assertIn('name', products[0])

    def test_read_csv_invalid(self):
        """Tester la lecture d'un fichier CSV invalide"""
        products = read_csv('tests/non_existent_file.csv')
        self.assertIsNone(products)

if __name__ == "__main__":
    unittest.main()
