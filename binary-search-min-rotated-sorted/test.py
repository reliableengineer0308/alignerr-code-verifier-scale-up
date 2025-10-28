import unittest
import sys
from io import StringIO
from solution import find_min_rotated, solve_min_rotated

class TestMinRotated(unittest.TestCase):
    
    def test_case1(self):
        nums = [3, 4, 5, 1, 2]
        result = find_min_rotated(nums)
        self.assertEqual(result, 1)
    
    def test_case2(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        result = find_min_rotated(nums)
        self.assertEqual(result, 0)
    
    def test_case3(self):
        nums = [1, 1, 1, 0, 1, 1]
        result = find_min_rotated(nums)
        self.assertEqual(result, 0)
    
    def test_sorted_array(self):
        nums = [1, 2, 3, 4, 5]
        result = find_min_rotated(nums)
        self.assertEqual(result, 1)
    
    def test_single_element(self):
        nums = [5]
        result = find_min_rotated(nums)
        self.assertEqual(result, 5)
    
    def test_full_integration(self):
        input_data = """3
5
3 4 5 1 2
7
4 5 6 7 0 1 2
6
1 1 1 0 1 1"""
        
        expected_output = [
            "Case #1: 1",
            "Case #2: 0", 
            "Case #3: 0"
        ]
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_min_rotated()
            self.assertEqual(results, expected_output)
        finally:
            sys.stdin = old_stdin

if __name__ == '__main__':
    unittest.main(verbosity=2)