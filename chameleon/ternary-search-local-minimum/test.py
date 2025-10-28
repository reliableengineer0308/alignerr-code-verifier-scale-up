import unittest
import sys
from io import StringIO
from solution import find_local_minimum, solve_local_minimum

class TestLocalMinimum(unittest.TestCase):
    
    def test_mountain_array(self):
        arr = [9, 7, 8, 6, 5, 4, 3]
        result = find_local_minimum(arr)
        # Local minima: 7, 6, 5, 4, 3
        self.assertIn(result, [7, 6, 5, 4, 3])
    
    def test_sorted_ascending(self):
        arr = [1, 2, 3, 4, 5]
        result = find_local_minimum(arr)
        self.assertEqual(result, 1)  # Only local minimum is first element
    
    def test_sorted_descending(self):
        arr = [5, 4, 3, 2, 1]
        result = find_local_minimum(arr)
        self.assertEqual(result, 1)  # Only local minimum is last element
    
    def test_valley_array(self):
        arr = [10, 2, 3, 1, 5, 6]
        result = find_local_minimum(arr)
        # Local minima: 2 or 1, both are valid
        self.assertIn(result, [2, 1])
    
    def test_single_element(self):
        arr = [5]
        result = find_local_minimum(arr)
        self.assertEqual(result, 5)  # Single element is trivially local minimum
    
    def test_full_integration(self):
        input_data = """3
7
9 7 8 6 5 4 3
5
1 2 3 4 5
6
10 2 3 1 5 6"""
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_local_minimum()
            # Check that we get exactly 3 results
            self.assertEqual(len(results), 3)
            # Check format and known results
            self.assertTrue(results[0].startswith("Case #1:"))
            self.assertEqual(results[1], "Case #2: 1")
            # For case 3, either 2 or 1 is acceptable
            self.assertTrue(results[2] in ["Case #3: 2", "Case #3: 1"])
        finally:
            sys.stdin = old_stdin

if __name__ == '__main__':
    unittest.main(verbosity=2)