import unittest
import sys
from io import StringIO
from solution import BellNumbers, solve_bell_numbers

class TestBellNumbers(unittest.TestCase):
    
    def test_basic_cases(self):
        calculator = BellNumbers(10)
        
        self.assertEqual(calculator.get_bell(0, 1000000007), 1)
        self.assertEqual(calculator.get_bell(1, 1000000007), 1)
        self.assertEqual(calculator.get_bell(2, 1000000007), 2)
        self.assertEqual(calculator.get_bell(3, 1000000007), 5)
        self.assertEqual(calculator.get_bell(4, 1000000007), 15)
        self.assertEqual(calculator.get_bell(5, 1000000007), 52)
    
    def test_known_sequence(self):
        calculator = BellNumbers(6)
        bell_seq = calculator.compute_bell(1000000007)
        
        expected = [1, 1, 2, 5, 15, 52, 203]
        for i, val in enumerate(expected):
            self.assertEqual(bell_seq[i], val)
    
    def test_different_modulus(self):
        calculator = BellNumbers(5)
        
        self.assertEqual(calculator.get_bell(3, 100), 5)
        self.assertEqual(calculator.get_bell(4, 10), 5)  # 15 mod 10 = 5
        self.assertEqual(calculator.get_bell(5, 50), 2)  # 52 mod 50 = 2
    
    def test_full_integration(self):
        input_data = """6
0 1000000007
1 1000000007
2 1000000007
3 1000000007
4 1000000007
5 1000000007"""
        
        expected_output = ["1", "1", "2", "5", "15", "52"]
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_bell_numbers()
            self.assertEqual(results, expected_output)
        finally:
            sys.stdin = old_stdin

if __name__ == '__main__':
    unittest.main(verbosity=2)