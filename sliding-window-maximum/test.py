import unittest
from solution import max_sliding_window

class TestSlidingWindowMaximum(unittest.TestCase):
    
    def test_basic_case(self):
        nums = [1, 3, -1, -3, 5, 3, 6, 7]
        k = 3
        self.assertEqual(max_sliding_window(nums, k), [3, 3, 5, 5, 6, 7])
    
    def test_single_element_window(self):
        nums = [1, 2, 3, 4, 5]
        k = 1
        self.assertEqual(max_sliding_window(nums, k), [1, 2, 3, 4, 5])
    
    def test_window_size_equals_array(self):
        nums = [9, 8, 7, 6]
        k = 4
        self.assertEqual(max_sliding_window(nums, k), [9])
    
    def test_decreasing_sequence(self):
        nums = [5, 4, 3, 2, 1]
        k = 3
        self.assertEqual(max_sliding_window(nums, k), [5, 4, 3])
    
    def test_empty_array(self):
        nums = []
        k = 3
        self.assertEqual(max_sliding_window(nums, k), [])
    
    def test_complex_case_with_duplicates(self):
        nums = [4, 2, 4, 3, 2, 5, 7, 3, 8, 1]
        k = 4
        self.assertEqual(max_sliding_window(nums, k), [4, 4, 5, 7, 7, 8, 8])
    
    def test_all_negative_numbers(self):
        nums = [-3, -1, -2, -5, -4, -6]
        k = 2
        self.assertEqual(max_sliding_window(nums, k), [-1, -1, -2, -4, -4])
    
    def test_large_window_with_small_array(self):
        nums = [10, 20, 30, 40, 50]
        k = 5
        self.assertEqual(max_sliding_window(nums, k), [50])
    
    def test_random_sequence(self):
        nums = [1, -1, 2, -2, 3, -3, 4, -4]
        k = 3
        self.assertEqual(max_sliding_window(nums, k), [2, 2, 3, 3, 4, 4])

if __name__ == '__main__':
    unittest.main()