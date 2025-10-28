import unittest
import sys
from io import StringIO
from solution import search_range, solve_first_last_position

class TestFirstLastPosition(unittest.TestCase):
    
    def test_found_multiple(self):
        nums = [5, 7, 7, 8, 8, 10]
        target = 8
        result = search_range(nums, target)
        self.assertEqual(result, [3, 4])
    
    def test_not_found(self):
        nums = [1, 2, 3, 4, 5]
        target = 6
        result = search_range(nums, target)
        self.assertEqual(result, [-1, -1])
    
    def test_all_same(self):
        nums = [4, 4, 4, 4, 4, 4, 4]
        target = 4
        result = search_range(nums, target)
        self.assertEqual(result, [0, 6])
    
    def test_single_occurrence(self):
        nums = [1, 3, 5, 7, 9]
        target = 5
        result = search_range(nums, target)
        self.assertEqual(result, [2, 2])
    
    def test_empty_array(self):
        nums = []
        target = 5
        result = search_range(nums, target)
        self.assertEqual(result, [-1, -1])
    
    def test_full_integration(self):
        input_data = """3
6 8
5 7 7 8 8 10
5 6
1 2 3 4 5
7 4
4 4 4 4 4 4 4"""
        
        expected_output = [
            "Case #1: 3 4",
            "Case #2: -1 -1", 
            "Case #3: 0 6"
        ]
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_first_last_position()
            self.assertEqual(results, expected_output)
        finally:
            sys.stdin = old_stdin

if __name__ == '__main__':
    unittest.main(verbosity=2)