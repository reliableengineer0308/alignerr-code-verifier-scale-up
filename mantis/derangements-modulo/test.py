import unittest
import sys
from io import StringIO
from solution import Derangements, solve_derangements

class TestDerangements(unittest.TestCase):
    
    def test_basic_cases(self):
        calculator = Derangements(10)
        
        self.assertEqual(calculator.get_derangement(0, 1000000007), 1)
        self.assertEqual(calculator.get_derangement(1, 1000000007), 0)
        self.assertEqual(calculator.get_derangement(2, 1000000007), 1)
        self.assertEqual(calculator.get_derangement(3, 1000000007), 2)
        self.assertEqual(calculator.get_derangement(4, 1000000007), 9)
    
    def test_known_sequence(self):
        calculator = Derangements(6)
        calculator.compute_derangements(1000000007)
        
        expected = [1, 0, 1, 2, 9, 44, 265]
        for i, val in enumerate(expected):
            self.assertEqual(calculator.derangements[i], val)
    
    def test_different_modulus(self):
        calculator = Derangements(5)
        
        self.assertEqual(calculator.get_derangement(3, 100), 2)
        self.assertEqual(calculator.get_derangement(4, 10), 9)
        self.assertEqual(calculator.get_derangement(5, 100), 44)
    
    def test_full_integration(self):
        input_data = """5
0 1000000007
1 1000000007
2 1000000007
3 1000000007
4 1000000007"""
        
        expected_output = ["1", "0", "1", "2", "9"]
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_derangements()
            self.assertEqual(results, expected_output)
        finally:
            sys.stdin = old_stdin

if __name__ == '__main__':
    unittest.main(verbosity=2)