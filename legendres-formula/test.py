import unittest
import sys
from io import StringIO
from solution import legendre_exponent, solve_legendre_formula

class TestLegendreFormula(unittest.TestCase):
    
    def test_basic_cases(self):
        self.assertEqual(legendre_exponent(10, 2), 8)
        self.assertEqual(legendre_exponent(10, 3), 4)
        self.assertEqual(legendre_exponent(10, 5), 2)
        self.assertEqual(legendre_exponent(100, 2), 97)
    
    def test_edge_cases(self):
        self.assertEqual(legendre_exponent(0, 2), 0)
        self.assertEqual(legendre_exponent(1, 2), 0)
        self.assertEqual(legendre_exponent(2, 2), 1)
        self.assertEqual(legendre_exponent(5, 5), 1)
    
    def test_large_values(self):
        self.assertEqual(legendre_exponent(1000000000, 2), 999999987)
        
        # Test with large prime
        self.assertEqual(legendre_exponent(100, 97), 1) 
    
    def test_full_integration(self):
        input_data = """5
10 2
10 3
10 5
100 2
1000000000 2"""
        
        expected_output = ["8", "4", "2", "97", "999999987"]
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_legendre_formula()
            self.assertEqual(results, expected_output)
        finally:
            sys.stdin = old_stdin

if __name__ == '__main__':
    unittest.main(verbosity=2)