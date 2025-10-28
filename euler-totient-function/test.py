import unittest
import sys
from io import StringIO
from solution import EulerTotient, solve_euler_totient

class TestEulerTotient(unittest.TestCase):
    
    def test_basic_cases(self):
        calculator = EulerTotient(100)
        calculator.compute_phi()
        
        self.assertEqual(calculator.get_phi(1), 1)
        self.assertEqual(calculator.get_phi(2), 1)
        self.assertEqual(calculator.get_phi(9), 6)
        self.assertEqual(calculator.get_phi(10), 4)
        self.assertEqual(calculator.get_phi(100), 40)
    
    def test_prime_numbers(self):
        calculator = EulerTotient(1000000)
        calculator.compute_phi()
        
        self.assertEqual(calculator.get_phi(999983), 999982)
        self.assertEqual(calculator.get_phi(17), 16)
        self.assertEqual(calculator.get_phi(13), 12)
    
    def test_composite_numbers(self):
        calculator = EulerTotient(1000)
        calculator.compute_phi()
        
        self.assertEqual(calculator.get_phi(12), 4)
        self.assertEqual(calculator.get_phi(30), 8)
        self.assertEqual(calculator.get_phi(49), 42)
    
    def test_full_integration(self):
        input_data = """6
1
2
9
10
100
999983"""
        
        expected_output = ["1", "1", "6", "4", "40", "999982"]
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_euler_totient()
            self.assertEqual(results, expected_output)
        finally:
            sys.stdin = old_stdin

if __name__ == '__main__':
    unittest.main(verbosity=2)