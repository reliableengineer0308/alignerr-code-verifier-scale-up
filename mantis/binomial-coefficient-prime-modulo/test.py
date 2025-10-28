import unittest
import sys
from io import StringIO
from solution import BinomialCoefficient, solve_binomial_coefficient

class TestBinomialCoefficient(unittest.TestCase):
    
    def test_basic_cases(self):
        calculator = BinomialCoefficient(10, 1000000007)
        calculator.precompute()
        
        self.assertEqual(calculator.nCr(5, 2), 10)
        self.assertEqual(calculator.nCr(10, 3), 120)
        self.assertEqual(calculator.nCr(5, 6), 0)
        self.assertEqual(calculator.nCr(0, 0), 1)
    
    def test_large_values(self):
        calculator = BinomialCoefficient(1000, 1000000007)
        calculator.precompute()
        
        # C(1000, 500) mod 1000000007 = 159835829
        self.assertEqual(calculator.nCr(1000, 500), 159835829)
    
    def test_edge_cases(self):
        calculator = BinomialCoefficient(10, 1000000007)
        calculator.precompute()
        
        self.assertEqual(calculator.nCr(0, 0), 1)
        self.assertEqual(calculator.nCr(5, 0), 1)
        self.assertEqual(calculator.nCr(5, 5), 1)
        self.assertEqual(calculator.nCr(5, 10), 0)
    
    def test_full_integration(self):
        input_data = """4
5 2 1000000007
10 3 1000000007
1000 500 1000000007
5 6 1000000007"""
        
        expected_output = ["10", "120", "159835829", "0"]
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_binomial_coefficient()
            self.assertEqual(results, expected_output)
        finally:
            sys.stdin = old_stdin

if __name__ == '__main__':
    unittest.main(verbosity=2)