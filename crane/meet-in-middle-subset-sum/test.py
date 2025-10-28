import unittest
import sys
from io import StringIO
from solution import closest_subset_sum, solve_meet_in_middle

class TestMeetInMiddle(unittest.TestCase):
    
    def test_exact_match(self):
        nums = [1, 2, 3, 4, 5]
        target = 10
        result = closest_subset_sum(nums, target)
        self.assertEqual(result, 10)  # [1,2,3,4] or [2,3,5]
    
    def test_closest_match(self):
        nums = [-1, 2, 3, 4]
        target = 7
        result = closest_subset_sum(nums, target)
        self.assertEqual(result, 7)  # [3,4] sums to 7
    
    def test_negative_numbers(self):
        nums = [-5, -2, 3, 8]
        target = 1
        result = closest_subset_sum(nums, target)
        self.assertEqual(result, 1)  # [-2,3] sums to 1
    
    def test_large_target(self):
        nums = [10, 20, 30, 40, 50, 60]
        target = 100
        result = closest_subset_sum(nums, target)
        self.assertEqual(result, 100)  # [10,20,30,40]
    
    def test_empty_subset(self):
        nums = [1, 2, 3]
        target = 0
        result = closest_subset_sum(nums, target)
        self.assertEqual(result, 0)  # Empty subset
    
    def test_no_exact_match(self):
        nums = [1, 3, 5]
        target = 4
        result = closest_subset_sum(nums, target)
        # Possible sums: 0,1,3,4,5,6,8,9
        # Closest to 4: 4 ([1,3]) has difference 0
        self.assertEqual(result, 4)  # [1,3] sums to 4
    
    def test_closest_but_not_exact(self):
        nums = [2, 4, 6]
        target = 5
        result = closest_subset_sum(nums, target)
        # Possible sums: 0,2,4,6,8,10,12
        # Closest to 5: 4 or 6, both have difference 1
        # Should pick the smaller one (4)
        self.assertEqual(result, 4)
    
    def test_full_integration(self):
        input_data = """3
5 10
1 2 3 4 5
4 7
-1 2 3 4
6 100
10 20 30 40 50 60"""
        
        expected_output = [
            "Case #1: 10",
            "Case #2: 7", 
            "Case #3: 100"
        ]
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_meet_in_middle()
            self.assertEqual(results, expected_output)
        finally:
            sys.stdin = old_stdin

if __name__ == '__main__':
    unittest.main(verbosity=2)