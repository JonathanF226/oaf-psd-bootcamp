import unittest
from is_prime import is_prime

class PrimeTesting(unittest.TestCase):
    def test_always_passes(self):
        self.assertTrue(True)
    
    def test_prime_number(self):
        self.assertTrue(is_prime(37))

    def test_non_prime_number(self):
        self.assertFalse(is_prime(55))

    def test_negative_number(self):
        self.assertFalse(is_prime(-90))

    def test_not_a_number(self):
        self.assertFalse(is_prime(None))

    def test_string(self):
        self.assertFalse(is_prime("100"))

if __name__ == "__main__":
    unittest.main()