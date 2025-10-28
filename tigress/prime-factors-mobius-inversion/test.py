import unittest
import sys
from io import StringIO
from solution import PrimeFactorCounter, solve_prime_factors_count

class TestPrimeFactorsCount(unittest.TestCase):
    
    def test_basic_cases(self):
        counter = PrimeFactorCounter(100)
        
        # Test small values - omega should count distinct prime factors
        self.assertEqual(counter.omega[1], 0)
        self.assertEqual(counter.omega[2], 1)
        self.assertEqual(counter.omega[4], 1)
        self.assertEqual(counter.omega[6], 2)
        self.assertEqual(counter.omega[12], 2)
    
    def test_counting(self):
        counter = PrimeFactorCounter(100)

        count_k1 = sum(1 for i in range(1, 11) if counter.omega[i] == 1)
        self.assertEqual(count_k1, 7)  # 2,3,4,5,7,8,9
        
        count_k2 = sum(1 for i in range(1, 11) if counter.omega[i] == 2)
        self.assertEqual(count_k2, 2)  # 6,10
    
    def test_edge_cases(self):
        counter = PrimeFactorCounter(100)
        
        # k = 0: only number 1
        count_k0 = sum(1 for i in range(1, 11) if counter.omega[i] == 0)
        self.assertEqual(count_k0, 1)
        
        # k larger than maximum possible
        count_large_k = sum(1 for i in range(1, 101) if counter.omega[i] == 10)
        self.assertEqual(count_large_k, 0)
    
    def test_known_values(self):
        """test_known_values"""
        counter = PrimeFactorCounter(1000)

        primes_up_to_10 = sum(1 for i in range(2, 11) if counter.omega[i] == 1 and i in [2,3,5,7])
        self.assertEqual(primes_up_to_10, 4)

        count_k2_100 = sum(1 for i in range(1, 101) if counter.omega[i] == 2)
        self.assertEqual(count_k2_100, 56)
    
    def test_full_integration(self):
        input_data = """5
10 1
10 2
100 2
1000 3
1000000 4"""

        expected_output = ["7", "2", "56", "275", "208034"]
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_prime_factors_count()
            self.assertEqual(results, expected_output)
        finally:
            sys.stdin = old_stdin

if __name__ == '__main__':
    unittest.main(verbosity=2)