import unittest
import sys
from io import StringIO
from solution import MultinomialCalculator, solve_multinomial

class TestMultinomialCoefficients(unittest.TestCase):
    
    def test_basic_cases(self):
        calculator = MultinomialCalculator(10)
        
        self.assertEqual(calculator.get_multinomial(6, [2, 2, 2], 1000000007), 90)
        self.assertEqual(calculator.get_multinomial(8, [3, 2, 2, 1], 1000000007), 1680)
        self.assertEqual(calculator.get_multinomial(10, [5, 5], 1000000007), 252)
        self.assertEqual(calculator.get_multinomial(5, [2, 2, 1], 1000000007), 30)
    
    def test_edge_cases(self):
        calculator = MultinomialCalculator(10)
        
        # Single group
        self.assertEqual(calculator.get_multinomial(5, [5], 1000000007), 1)
        # All groups of size 1
        self.assertEqual(calculator.get_multinomial(3, [1, 1, 1], 1000000007), 6)  # 3! = 6
    
    def test_different_modulus(self):
        calculator = MultinomialCalculator(10)
        
        self.assertEqual(calculator.get_multinomial(6, [2, 2, 2], 100), 90)
        self.assertEqual(calculator.get_multinomial(8, [3, 2, 2, 1], 1000), 1680 % 1000)  # 1680 mod 1000 = 680
        self.assertEqual(calculator.get_multinomial(8, [3, 2, 2, 1], 10), 0)  # 1680 mod 10 = 0
    
    def test_full_integration(self):
        input_data = """4
6 1000000007
3
2 2 2
8 1000000007
4
3 2 2 1
10 1000000007
2
5 5
5 1000000007
3
2 2 1"""
        
        expected_output = ["90", "1680", "252", "30"]
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_multinomial()
            self.assertEqual(results, expected_output)
        finally:
            sys.stdin = old_stdin

if __name__ == '__main__':
    unittest.main(verbosity=2)