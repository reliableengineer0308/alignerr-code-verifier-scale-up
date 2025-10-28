import unittest
import sys
from io import StringIO
from solution import PrimeSieve, solve_prime_generation

class TestPrimeGeneration(unittest.TestCase):
    
    def test_basic_cases(self):
        sieve = PrimeSieve(100)
        sieve.generate_primes()
        
        self.assertEqual(sieve.get_primes_up_to(20), [2, 3, 5, 7, 11, 13, 17, 19])
        self.assertEqual(sieve.get_primes_up_to(50), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47])
    
    def test_small_numbers(self):
        sieve = PrimeSieve(10)
        sieve.generate_primes()
        
        self.assertEqual(sieve.get_primes_up_to(2), [2])
        self.assertEqual(sieve.get_primes_up_to(10), [2, 3, 5, 7])
    
    def test_large_limit(self):
        sieve = PrimeSieve(1000000)
        sieve.generate_primes()
        
        # Check number of primes up to 1000000 (known value: 78498)
        primes = sieve.get_primes_up_to(1000000)
        self.assertEqual(len(primes), 78498)
        
        # Check first few primes
        self.assertEqual(primes[:10], [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])
    
    def test_full_integration(self):
        input_data = """2
20
50"""
        
        expected_output = [
            "2 3 5 7 11 13 17 19",
            "2 3 5 7 11 13 17 19 23 29 31 37 41 43 47"
        ]
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_prime_generation()
            self.assertEqual(results, expected_output)
        finally:
            sys.stdin = old_stdin

if __name__ == '__main__':
    unittest.main(verbosity=2)