import unittest
import sys
from io import StringIO
from solution import modular_exponentiation, solve_modular_exponentiation

class TestModularExponentiation(unittest.TestCase):
    
    def test_basic_cases(self):
        self.assertEqual(modular_exponentiation(2, 10, 1000000007), 1024)
        self.assertEqual(modular_exponentiation(3, 5, 13), 9)
        self.assertEqual(modular_exponentiation(0, 0, 100), 1)
        self.assertEqual(modular_exponentiation(0, 10, 100), 0)
    
    def test_large_exponents(self):
        self.assertEqual(modular_exponentiation(123456789, 987654321, 1000000007), 652541198)
        
        # Test with modulus 1
        self.assertEqual(modular_exponentiation(5, 10, 1), 0)
        self.assertEqual(modular_exponentiation(0, 0, 1), 0)
    
    def test_edge_cases(self):
        self.assertEqual(modular_exponentiation(1, 0, 100), 1)
        self.assertEqual(modular_exponentiation(1, 1000000000, 100), 1)
        self.assertEqual(modular_exponentiation(1000000000, 1000000000, 1000000007), 312556845)
    
    def test_full_integration(self):
        input_data = """5
2 10 1000000007
3 5 13
0 0 100
0 10 100
123456789 987654321 1000000007"""
        
        expected_output = ["1024", "9", "1", "0", "652541198"]
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_modular_exponentiation()
            self.assertEqual(results, expected_output)
        finally:
            sys.stdin = old_stdin

if __name__ == '__main__':
    unittest.main(verbosity=2)