import unittest
import sys
from io import StringIO
from solution import StirlingNumbers, solve_stirling_numbers

class TestStirlingNumbers(unittest.TestCase):
    
    def test_basic_cases(self):
        calculator = StirlingNumbers(10)
        
        self.assertEqual(calculator.get_stirling(3, 2, 1000000007), 3)
        self.assertEqual(calculator.get_stirling(4, 2, 1000000007), 7)
        self.assertEqual(calculator.get_stirling(5, 3, 1000000007), 25)
        self.assertEqual(calculator.get_stirling(0, 0, 1000000007), 1)
        self.assertEqual(calculator.get_stirling(4, 5, 1000000007), 0)
    
    def test_edge_cases(self):
        calculator = StirlingNumbers(5)
        
        self.assertEqual(calculator.get_stirling(1, 1, 1000000007), 1)
        self.assertEqual(calculator.get_stirling(5, 1, 1000000007), 1)
        self.assertEqual(calculator.get_stirling(5, 5, 1000000007), 1)
        self.assertEqual(calculator.get_stirling(5, 6, 1000000007), 0)
    
    def test_different_modulus(self):
        calculator = StirlingNumbers(5)
        
        self.assertEqual(calculator.get_stirling(3, 2, 100), 3)
        self.assertEqual(calculator.get_stirling(4, 2, 10), 7)
        self.assertEqual(calculator.get_stirling(5, 3, 20), 5)  # 25 mod 20 = 5
    
    def test_full_integration(self):
        input_data = """5
3 2 1000000007
4 2 1000000007
5 3 1000000007
0 0 1000000007
4 5 1000000007"""
        
        expected_output = ["3", "7", "25", "1", "0"]
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_stirling_numbers()
            self.assertEqual(results, expected_output)
        finally:
            sys.stdin = old_stdin

if __name__ == '__main__':
    unittest.main(verbosity=2)