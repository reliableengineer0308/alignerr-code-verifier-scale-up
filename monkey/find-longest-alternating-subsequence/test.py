import unittest
from solution import longest_alternating_subsequence

class TestLongestAlternatingSubsequence(unittest.TestCase):
    
    def test_basic_alternating(self):
        """Test with natural alternating pattern."""
        result = longest_alternating_subsequence([1, 5, 4, 3, 6])
        self.assertEqual(result, 4)  # [1,5,4,6] or similar
    
    def test_all_equal(self):
        """Test when all elements are the same."""
        result = longest_alternating_subsequence([2, 2, 2])
        self.assertEqual(result, 1)  # No alternation possible
    
    def test_strictly_decreasing(self):
        """Test strictly decreasing array."""
        result = longest_alternating_subsequence([10, 9, 8, 7, 6, 5])
        self.assertEqual(result, 2)  # Best: any two adjacent
    
    def test_strictly_increasing(self):
        """Test strictly increasing array."""
        result = longest_alternating_subsequence([1, 2, 3, 4, 5])
        self.assertEqual(result, 2)  # Best: first two
    
    def test_single_element(self):
        """Test minimal input (1 element)."""
        result = longest_alternating_subsequence([42])
        self.assertEqual(result, 1)
    
    def test_two_elements_different(self):
        """Test two different elements."""
        result = longest_alternating_subsequence([1, 2])
        self.assertEqual(result, 2)  # 1 < 2 → valid
    
    def test_two_elements_same(self):
        """Test two equal elements."""
        result = longest_alternating_subsequence([3, 3])
        self.assertEqual(result, 1)  # Equal → no alternation
    
    def test_complex_pattern(self):
        """Test complex alternating pattern."""
        result = longest_alternating_subsequence([1, 3, 2, 5, 4, 7, 6])
        self.assertEqual(result, 7)  # Perfect alternation: < > < > < >
    
    def test_empty_array(self):
        """Test empty input."""
        result = longest_alternating_subsequence([])
        self.assertEqual(result, 0)
    
    def test_plateau_handling(self):
        """Test handling of plateaus (equal adjacent values)."""
        result = longest_alternating_subsequence([1, 1, 2, 2, 3, 3])
        self.assertEqual(result, 2)  # Best: 1 < 2 or 2 < 3

if __name__ == "__main__":
    unittest.main()
