import unittest
import sys
from io import StringIO
from solution import ternary_search_max, quadratic_function, solve_ternary_search

class TestTernarySearch(unittest.TestCase):
    
    def test_quadratic_function(self):
        # Test function evaluation
        result = quadratic_function(0, 1, 0, 0)
        self.assertEqual(result, 0)
        
        result = quadratic_function(1, 1, 0, 0)
        self.assertEqual(result, -1)
        
        result = quadratic_function(2, 2, 8, 1)
        self.assertEqual(result, -8 + 16 + 1)  # -2*4 + 8*2 + 1 = -8 + 16 + 1 = 9
    
    def test_simple_peak_center(self):
        # f(x) = -x², peak at x=0
        result = ternary_search_max(-5, 5, 1, 0, 0)
        self.assertAlmostEqual(result, 0.0, places=6)
    
    def test_shifted_peak(self):
        # f(x) = -2x² + 8x + 1, peak at x=2
        result = ternary_search_max(-5, 5, 2, 8, 1)
        self.assertAlmostEqual(result, 2.0, places=6)
    
    def test_boundary_case(self):
        # f(x) = -0.5x² -10x + 100, peak at x=-10, but range is [1,20]
        # So maximum at left boundary x=1
        result = ternary_search_max(1, 20, 0.5, -10, 100)
        self.assertAlmostEqual(result, 1.0, places=6)
    
    def test_full_integration(self):
        input_data = """3
0.0 10.0
1.0 0.0 0.0
-5.0 5.0
2.0 8.0 1.0
1.0 20.0
0.5 -10.0 100.0"""
        
        expected_output = [
            "Case #1: 0.000000",
            "Case #2: 2.000000", 
            "Case #3: 1.000000"
        ]
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_ternary_search()
            self.assertEqual(results, expected_output)
        finally:
            sys.stdin = old_stdin
    
    def test_precision(self):
        # Test that ternary search achieves required precision
        result = ternary_search_max(0, 10, 1, 0, 0, precision=1e-7)
        self.assertAlmostEqual(result, 0.0, delta=1e-6)

if __name__ == '__main__':
    unittest.main(verbosity=2)