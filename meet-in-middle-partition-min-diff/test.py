import unittest
import sys
from io import StringIO
from solution import min_partition_difference, solve_min_partition_diff

class TestMinPartitionDiff(unittest.TestCase):
    
    def test_case1(self):
        nums = [1, 2, 3, 4, 5]
        result = min_partition_difference(nums)
        self.assertEqual(result, 1)
    
    def test_case2(self):
        nums = [1, 1, 1, 1]
        result = min_partition_difference(nums)
        # Total sum = 4, best partition: [1,1] and [1,1] gives difference 0
        self.assertEqual(result, 0)
    
    def test_case3(self):
        nums = [10, 20, 30]
        result = min_partition_difference(nums)
        # Total sum = 60, best partition: [10,20] and [30] gives difference 0
        self.assertEqual(result, 0)
    
    def test_negative_numbers(self):
        nums = [-1, 1]
        result = min_partition_difference(nums)
        # Total sum = 0, best partition: [-1] and [1] gives difference |(-1) - 1| = 2
        # Or [] and [-1,1] gives |0 - 0| = 0
        self.assertEqual(result, 0)
    
    def test_single_element(self):
        nums = [5]
        result = min_partition_difference(nums)
        # One subset must be empty, difference = |5 - 0| = 5
        self.assertEqual(result, 5)
    
    def test_full_integration(self):
        input_data = """3
5
1 2 3 4 5
4
1 1 1 1
3
10 20 30"""
        
        expected_output = [
            "Case #1: 1",
            "Case #2: 0", 
            "Case #3: 0"
        ]
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_min_partition_diff()
            self.assertEqual(results, expected_output)
        finally:
            sys.stdin = old_stdin

if __name__ == '__main__':
    unittest.main(verbosity=2)