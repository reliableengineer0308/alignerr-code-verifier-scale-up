import unittest
from solution import count_inversions

class TestCountInversions(unittest.TestCase):

    
    def test_empty_array(self):
        """Test with empty array."""
        self.assertEqual(count_inversions([]), 0)
    
    
    def test_single_element(self):
        """Test array with one element (no possible inversions)."""
        self.assertEqual(count_inversions([42]), 0)
        self.assertEqual(count_inversions([-5]), 0)
    
    
    def test_sorted_array(self):
        """Test already sorted array (no inversions)."""
        self.assertEqual(count_inversions([1, 2, 3, 4, 5]), 0)
        self.assertEqual(count_inversions(list(range(100))), 0)
        self.assertEqual(count_inversions([0, 1]), 0)
    
    
    def test_reverse_sorted(self):
        """Test reverse-sorted array (maximum inversions: n*(n-1)/2)."""
        # n=4: 4*3/2 = 6 inversions
        arr = [4, 3, 2, 1]
        expected = 6
        self.assertEqual(count_inversions(arr), expected)
        
        # n=5: 5*4/2 = 10 inversions
        arr = [5, 4, 3, 2, 1]
        expected = 10
        self.assertEqual(count_inversions(arr), expected)
    
    def test_example_1(self):
        """Test example: [2, 4, 1, 3, 5] → 3 inversions."""
        # Inversions: (2,1), (4,1), (4,3)
        arr = [2, 4, 1, 3, 5]
        self.assertEqual(count_inversions(arr), 3)
    
    def test_all_equal_elements(self):
        """Test array where all elements are equal (no inversions)."""
        self.assertEqual(count_inversions([3, 3, 3, 3]), 0)
        self.assertEqual(count_inversions([0, 0, 0]), 0)
        self.assertEqual(count_inversions([-1, -1]), 0)
   
    def test_small_arrays(self):
        """Test small arrays with known inversion counts."""
        # [1,3,2] → (3,2) → 1 inversion
        self.assertEqual(count_inversions([1, 3, 2]), 1)
        
        # [3,1,2] → (3,1), (3,2) → 2 inversions
        self.assertEqual(count_inversions([3, 1, 2]), 2)
        
        # [2,1] → (2,1) → 1 inversion
        self.assertEqual(count_inversions([2, 1]), 1)
    
    def test_large_random_array(self):
        """Test performance on a large shuffled array."""
        import random
        # Generate large random array
        arr = list(range(1000))
        random.shuffle(arr)
        
        result = count_inversions(arr)
        
        # Should be non-negative and within theoretical max
        self.assertGreaterEqual(result, 0)
        max_possible = len(arr) * (len(arr) - 1) // 2
        self.assertLessEqual(result, max_possible)
    
    def test_negative_numbers(self):
        """Test arrays with negative numbers."""
        # [-1, -3, -2] → (-1,-3), (-1,-2), (-3,-2)? No: -3 < -2
        # Actually: (-1,-3), (-1,-2) → but -1 > -3 and -1 > -2 → 2 inversions
        # Wait: -1 > -3 → inversion, -1 > -2 → inversion, but -3 < -2 → no inversion
        # So only (index0,index1) and (index0,index2) → 2 inversions
        arr = [-1, -3, -2]
        # -1 at index0 > -3 at index1 → inversion
        # -1 at index0 > -2 at index2 → inversion
        # -3 at index1 < -2 at index2 → no inversion
        self.assertEqual(count_inversions(arr), 2)
        
        # Another example: [-5, -1, -10] → (-5,-10), (-1,-10) → 2 inversions
        arr = [-5, -1, -10]
        self.assertEqual(count_inversions(arr), 2)
    
    def test_mixed_positive_negative(self):
        """Test arrays with mixed positive and negative numbers."""
        # [-2, 1, -1] → (-2,-1)? No: -2 < -1. (1,-1) → yes
        # Only (1 at index1, -1 at index2) → 1 inversion
        arr = [-2, 1, -1]
        self.assertEqual(count_inversions(arr), 1)
        
        # [3, -1, 2, -5] → (3,-1), (3,2)? No, (3,-5), (-1,-5), (2,-5)
        # Valid: (3,-1), (3,-5), (-1,-5)? -1 > -5 → yes, (2,-5) → 2 > -5 → yes
        # But check indices: 
        # (0,1): 3 > -1 → inversion
        # (0,3): 3 > -5 → inversion
        # (1,3): -1 > -5 → inversion
        # (2,3): 2 > -5 → inversion
        # Total: 4 inversions
        arr = [3, -1, 2, -5]
        self.assertEqual(count_inversions(arr), 5)
    
    def test_duplicate_values(self):
        """Test arrays with duplicate values."""
        # [2, 2, 1] → (2,1), (2,1) → 2 inversions (both 2s before 1)
        arr = [2, 2, 1]
        self.assertEqual(count_inversions(arr), 2)
        
        # [1, 2, 2] → no inversions
        arr = [1, 2, 2]
        self.assertEqual(count_inversions(arr), 0)
        
        # [5, 3, 3, 1] → (5,3), (5,3), (5,1), (3,1), (3,1) → 5 inversions
        arr = [5, 3, 3, 1]
        self.assertEqual(count_inversions(arr), 5)

if __name__ == '__main__':
    unittest.main()
