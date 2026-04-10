import unittest
from app import greet, farewell

class TestApp(unittest.TestCase):
    def test_greet(self):
        result = greet("Madan")
        self.assertIn("Madan", result)
        self.assertIn("AIDI 2004", result)

    def test_farewell(self):
        result = farewell("Madan")
        self.assertIn("Madan", result)

if __name__ == "__main__":
    unittest.main()