import unittest
import sys
from io import StringIO
from solution import MobiusFunction, solve_mobius_function

class TestMobiusFunction(unittest.TestCase):
    
    def test_basic_cases(self):
        calculator = MobiusFunction(100)
        
        self.assertEqual(calculator.get_mobius(1), 1)
        self.assertEqual(calculator.get_mobius(2), -1)
        self.assertEqual(calculator.get_mobius(4), 0)
        self.assertEqual(calculator.get_mobius(6), 1)
        self.assertEqual(calculator.get_mobius(12), 0)
        self.assertEqual(calculator.get_mobius(30), -1)
    
    def test_prime_numbers(self):
        calculator = MobiusFunction(1000)
        
        self.assertEqual(calculator.get_mobius(17), -1)
        self.assertEqual(calculator.get_mobius(19), -1)
        self.assertEqual(calculator.get_mobius(23), -1)
    
    def test_square_free(self):
        calculator = MobiusFunction(100)
        
        # Product of 2 distinct primes (even) → 1
        self.assertEqual(calculator.get_mobius(10), 1)  # 2*5
        self.assertEqual(calculator.get_mobius(15), 1)  # 3*5
        
        # Product of 3 distinct primes (odd) → -1
        self.assertEqual(calculator.get_mobius(30), -1)  # 2*3*5
        self.assertEqual(calculator.get_mobius(42), -1)  # 2*3*7
    
    def test_full_integration(self):
        input_data = """6
1
2
4
6
12
30"""
        
        expected_output = ["1", "-1", "0", "1", "0", "-1"]
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_mobius_function()
            self.assertEqual(results, expected_output)
        finally:
            sys.stdin = old_stdin

if __name__ == '__main__':
    unittest.main(verbosity=2)