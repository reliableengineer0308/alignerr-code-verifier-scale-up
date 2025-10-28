import unittest
import sys
from io import StringIO
from solution import CatalanNumbers, solve_catalan_numbers

class TestCatalanNumbers(unittest.TestCase):
    
    def test_basic_cases(self):
        calculator = CatalanNumbers(10)
        
        self.assertEqual(calculator.get_catalan(0, 1000000007), 1)
        self.assertEqual(calculator.get_catalan(1, 1000000007), 1)
        self.assertEqual(calculator.get_catalan(3, 1000000007), 5)
        self.assertEqual(calculator.get_catalan(5, 1000000007), 42)
        self.assertEqual(calculator.get_catalan(10, 1000000007), 16796)
    
    def test_known_sequence(self):
        calculator = CatalanNumbers(5)
        catalan_seq = calculator.compute_catalan_dp(1000000007)
        
        expected = [1, 1, 2, 5, 14, 42]
        for i, val in enumerate(expected):
            self.assertEqual(catalan_seq[i], val)
    
    def test_different_modulus(self):
        calculator = CatalanNumbers(5)
        
        self.assertEqual(calculator.get_catalan(3, 100), 5)
        self.assertEqual(calculator.get_catalan(4, 10), 4)  # 14 mod 10 = 4
        self.assertEqual(calculator.get_catalan(5, 100), 42)  # 42 mod 100 = 42
        
        # Test with small modulus
        self.assertEqual(calculator.get_catalan(4, 5), 4)  # 14 mod 5 = 4
        self.assertEqual(calculator.get_catalan(5, 40), 2)  # 42 mod 40 = 2
    
    def test_full_integration(self):
        input_data = """5
0 1000000007
1 1000000007
3 1000000007
5 1000000007
10 1000000007"""
        
        expected_output = ["1", "1", "5", "42", "16796"]
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_catalan_numbers()
            self.assertEqual(results, expected_output)
        finally:
            sys.stdin = old_stdin

if __name__ == '__main__':
    unittest.main(verbosity=2)