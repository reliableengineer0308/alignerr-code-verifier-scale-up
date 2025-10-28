import unittest
import sys
from io import StringIO
from solution import find_kth_sorted_arrays, solve_kth_element

class TestKthElement(unittest.TestCase):
    
    def test_case1(self):
        nums1 = [1, 3, 5, 7]
        nums2 = [2, 4, 6, 8]
        k = 4
        result = find_kth_sorted_arrays(nums1, nums2, k)
        self.assertEqual(result, 4)
    
    def test_case2(self):
        nums1 = [1, 2, 3]
        nums2 = [4, 5, 6]
        k = 3
        result = find_kth_sorted_arrays(nums1, nums2, k)
        self.assertEqual(result, 3)
    
    def test_case3(self):
        nums1 = [1, 2]
        nums2 = [3, 4]
        k = 2
        result = find_kth_sorted_arrays(nums1, nums2, k)
        self.assertEqual(result, 2)
    
    def test_one_empty_array(self):
        nums1 = []
        nums2 = [1, 2, 3]
        k = 2
        result = find_kth_sorted_arrays(nums1, nums2, k)
        self.assertEqual(result, 2)
    
    def test_same_elements(self):
        nums1 = [1, 1, 1]
        nums2 = [1, 1, 1]
        k = 4
        result = find_kth_sorted_arrays(nums1, nums2, k)
        self.assertEqual(result, 1)
    
    def test_full_integration(self):
        input_data = """3
4 4 4
1 3 5 7
2 4 6 8
3 3 3
1 2 3
4 5 6
2 2 2
1 2
3 4"""
        
        expected_output = [
            "Case #1: 4",
            "Case #2: 3", 
            "Case #3: 2"
        ]
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_kth_element()
            self.assertEqual(results, expected_output)
        finally:
            sys.stdin = old_stdin

if __name__ == '__main__':
    unittest.main(verbosity=2)