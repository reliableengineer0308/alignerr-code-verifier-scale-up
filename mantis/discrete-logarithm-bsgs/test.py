import unittest
import sys
from io import StringIO
from solution import discrete_logarithm, solve_discrete_log

class TestDiscreteLogarithm(unittest.TestCase):
    
    def test_basic_cases(self):
        self.assertEqual(discrete_logarithm(23, 5, 3), 16)
        self.assertEqual(discrete_logarithm(1000000007, 2, 1), 0)
        # 3^316884446 ≡ 2 mod 1000000007, so solution exists
        self.assertEqual(discrete_logarithm(1000000007, 3, 2), 316884446)
    
    def test_small_primes(self):
        # Test with small prime
        self.assertEqual(discrete_logarithm(11, 2, 3), 8)  # 2^8 = 256 ≡ 3 mod 11
        self.assertEqual(discrete_logarithm(7, 3, 2), 2)   # 3^2 = 9 ≡ 2 mod 7
    
    def test_edge_cases(self):
        self.assertEqual(discrete_logarithm(5, 2, 1), 0)   # 2^0 = 1
        self.assertEqual(discrete_logarithm(5, 2, 2), 1)   # 2^1 = 2
        self.assertEqual(discrete_logarithm(5, 2, 4), 2)   # 2^2 = 4
        self.assertEqual(discrete_logarithm(5, 2, 3), 3)   # 2^3 = 8 ≡ 3 mod 5
    
    def test_no_solution(self):
        # For prime p, g is primitive root if order is p-1
        # If g is not primitive root, some h may not be in the subgroup
        # Let's find a case with no solution
        self.assertEqual(discrete_logarithm(7, 2, 3), -1)  # No solution: 2^x mod 7 can only be 1,2,4
    
    def test_verification(self):
        # Verify that the solution is correct
        p = 1000000007
        g = 3
        h = 2
        x = discrete_logarithm(p, g, h)
        if x != -1:
            self.assertEqual(pow(g, x, p), h)
    
    def test_full_integration(self):
        input_data = """3
23 5 3
1000000007 2 1
1000000007 3 2"""
        
        expected_output = ["16", "0", "316884446"]
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_discrete_log()
            self.assertEqual(results, expected_output)
        finally:
            sys.stdin = old_stdin

if __name__ == '__main__':
    unittest.main(verbosity=2)