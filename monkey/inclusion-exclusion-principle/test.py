import unittest
import sys
from io import StringIO
from solution import inclusion_exclusion, solve_inclusion_exclusion

class TestInclusionExclusion(unittest.TestCase):
    
    def test_basic_cases(self):
        self.assertEqual(inclusion_exclusion(100, [2, 3]), 67)
        self.assertEqual(inclusion_exclusion(1000, [2, 3, 5]), 734)
    
    def test_single_prime(self):
        self.assertEqual(inclusion_exclusion(100, [2]), 50)
        self.assertEqual(inclusion_exclusion(100, [7]), 14)
    
    def test_large_n(self):
        self.assertEqual(inclusion_exclusion(10**9, [2, 3, 5, 7, 11, 13, 17, 19]), 828975977)
    
    def test_edge_cases(self):
        self.assertEqual(inclusion_exclusion(1, [2, 3]), 0)
        self.assertEqual(inclusion_exclusion(10, [11, 13]), 0)
    
    def test_full_integration(self):
        input_data = """2
100 2
2 3
1000 3
2 3 5"""
        
        expected_output = ["67", "734"]
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_inclusion_exclusion()
            self.assertEqual(results, expected_output)
        finally:
            sys.stdin = old_stdin

if __name__ == '__main__':
    unittest.main(verbosity=2)