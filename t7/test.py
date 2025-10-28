import unittest
import sys
from io import StringIO
from solution import find_lis

class TestLIS(unittest.TestCase):
    
    def test_example1(self):
        """Test the first example from prompt"""
        arr = [10, 9, 2, 5, 3, 7, 101, 18]
        length, sequence = find_lis(arr)
        
        self.assertEqual(length, 4)
        # Check if sequence is strictly increasing
        for i in range(len(sequence) - 1):
            self.assertLess(sequence[i], sequence[i + 1])
        # Check if all elements are from original array and in correct order
        idx = 0
        for num in sequence:
            found = False
            while idx < len(arr):
                if arr[idx] == num:
                    found = True
                    break
                idx += 1
            self.assertTrue(found, f"Element {num} not found in correct order")
    
    def test_example2(self):
        """Test the second example from prompt"""
        arr = [0, 8, 4, 12, 2, 10]
        length, sequence = find_lis(arr)
        
        self.assertEqual(length, 3)
        # Check if sequence is strictly increasing
        for i in range(len(sequence) - 1):
            self.assertLess(sequence[i], sequence[i + 1])
        # Check if all elements are from original array
        for num in sequence:
            self.assertIn(num, arr)
    
    def test_example3(self):
        """Test the third example from prompt"""
        arr = [3, 4, -1, 5, 8, 2, 3]
        length, sequence = find_lis(arr)
        
        self.assertEqual(length, 4)
        # Check if sequence is strictly increasing
        for i in range(len(sequence) - 1):
            self.assertLess(sequence[i], sequence[i + 1])
        # Check if all elements are from original array
        for num in sequence:
            self.assertIn(num, arr)
    
    def test_single_element(self):
        """Test with single element"""
        arr = [5]
        length, sequence = find_lis(arr)
        
        self.assertEqual(length, 1)
        self.assertEqual(sequence, [5])
    
    def test_decreasing_sequence(self):
        """Test with strictly decreasing sequence"""
        arr = [5, 4, 3, 2, 1]
        length, sequence = find_lis(arr)
        
        self.assertEqual(length, 1)
        self.assertEqual(len(sequence), 1)
    
    def test_increasing_sequence(self):
        """Test with strictly increasing sequence"""
        arr = [1, 2, 3, 4, 5]
        length, sequence = find_lis(arr)
        
        self.assertEqual(length, 5)
        self.assertEqual(sequence, [1, 2, 3, 4, 5])
    
    def test_with_duplicates(self):
        """Test with duplicate values"""
        arr = [1, 3, 3, 3, 2, 4, 4, 5]
        length, sequence = find_lis(arr)
        
        # Should be strictly increasing (no duplicates in LIS)
        for i in range(len(sequence) - 1):
            self.assertLess(sequence[i], sequence[i + 1])
        self.assertEqual(length, 4)  # e.g., [1, 3, 4, 5]
    
    def test_negative_numbers(self):
        """Test with negative numbers"""
        arr = [-5, -3, -1, -2, -4]
        length, sequence = find_lis(arr)
        
        self.assertEqual(length, 3)  # [-5, -3, -1]
        for i in range(len(sequence) - 1):
            self.assertLess(sequence[i], sequence[i + 1])
    
    def test_empty_array(self):
        """Test with empty array"""
        arr = []
        length, sequence = find_lis(arr)
        
        self.assertEqual(length, 0)
        self.assertEqual(sequence, [])

if __name__ == '__main__':
    unittest.main()