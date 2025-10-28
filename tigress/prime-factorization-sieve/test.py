import unittest
import sys
from io import StringIO
from solution import PrimeFactorizer, solve_prime_factorization

class TestPrimeFactorization(unittest.TestCase):
    
    def test_basic_cases(self):
        factorizer = PrimeFactorizer(100)
        
        self.assertEqual(factorizer.factorize(60), [(2, 2), (3, 1), (5, 1)])
        self.assertEqual(factorizer.factorize(17), [(17, 1)])
        self.assertEqual(factorizer.factorize(1), [(1, 1)])
        self.assertEqual(factorizer.factorize(100), [(2, 2), (5, 2)])
    
    def test_prime_numbers(self):
        factorizer = PrimeFactorizer(1000000)
        
        self.assertEqual(factorizer.factorize(999983), [(999983, 1)])
        self.assertEqual(factorizer.factorize(2), [(2, 1)])
        self.assertEqual(factorizer.factorize(3), [(3, 1)])
    
    def test_composite_numbers(self):
        factorizer = PrimeFactorizer(1000)
        
        self.assertEqual(factorizer.factorize(12), [(2, 2), (3, 1)])
        self.assertEqual(factorizer.factorize(30), [(2, 1), (3, 1), (5, 1)])
        self.assertEqual(factorizer.factorize(49), [(7, 2)])
    
    def test_full_integration(self):
        input_data = """5
60
17
1
100
999983"""
        
        expected_output = [
            "2^2 3^1 5^1",
            "17^1", 
            "1^1",
            "2^2 5^2",
            "999983^1"
        ]
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_prime_factorization()
            self.assertEqual(results, expected_output)
        finally:
            sys.stdin = old_stdin

if __name__ == '__main__':
    unittest.main(verbosity=2)