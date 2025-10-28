import unittest
import sys
from io import StringIO
from solution import pollard_rho, solve_pollard_rho

class TestPollardRho(unittest.TestCase):
    
    def test_basic_cases(self):
        # Test small composites
        self.assertIn(pollard_rho(15), [3, 5])
        self.assertIn(pollard_rho(91), [7, 13])
        self.assertIn(pollard_rho(10403), [101, 103])
    
    def test_even_numbers(self):
        self.assertEqual(pollard_rho(4), 2)
        self.assertEqual(pollard_rho(6), 2)
        self.assertEqual(pollard_rho(8), 2)
        self.assertEqual(pollard_rho(10), 2)
    
    def test_large_composites(self):
        # Test larger composites
        factor = pollard_rho(999999999999)
        self.assertTrue(999999999999 % factor == 0)
        self.assertTrue(factor > 1 and factor < 999999999999)
    
    def test_prime_numbers(self):
        # For prime numbers, should return the number itself
        self.assertEqual(pollard_rho(1000000000039), 1000000000039)
        self.assertEqual(pollard_rho(17), 17)
        self.assertEqual(pollard_rho(19), 19)
    
    def test_full_integration(self):
        input_data = """5
15
91
10403
999999999999
1000000000039"""
        
        # Since Pollard's Rho is randomized, we can only verify factors divide the numbers
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_pollard_rho()
            # Verify that each result is a valid factor
            test_cases = [15, 91, 10403, 999999999999, 1000000000039]
            for i, (n, factor_str) in enumerate(zip(test_cases, results)):
                factor = int(factor_str)
                self.assertTrue(n % factor == 0)
                self.assertTrue(factor > 1)
        finally:
            sys.stdin = old_stdin

if __name__ == '__main__':
    unittest.main(verbosity=2)