import unittest
from solution import search_rotated_array

class TestRotatedArraySearch(unittest.TestCase):
    
    def test_rotated_array(self):
        # Test rotated array
        nums = [4, 5, 6, 7, 0, 1, 2]
        self.assertEqual(search_rotated_array(nums, 0), 4)
        self.assertEqual(search_rotated_array(nums, 3), -1)
        self.assertEqual(search_rotated_array(nums, 7), 3)
    
    def test_sorted_array(self):
        # Test non-rotated sorted array
        nums = [1, 2, 3, 4, 5]
        self.assertEqual(search_rotated_array(nums, 3), 2)
        self.assertEqual(search_rotated_array(nums, 1), 0)
    
    def test_single_element(self):
        # Test single element
        nums = [5]
        self.assertEqual(search_rotated_array(nums, 5), 0)
        self.assertEqual(search_rotated_array(nums, 0), -1)
    
    def test_empty_array(self):
        # Test empty array
        nums = []
        self.assertEqual(search_rotated_array(nums, 5), -1)

if __name__ == '__main__':
    unittest.main()