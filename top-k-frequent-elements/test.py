import unittest
from solution import top_k_frequent


class TestTopKFrequent(unittest.TestCase):
    
    def test_basic_case(self):
        """Test with standard frequency distribution."""
        nums = [1, 1, 1, 2, 2, 3]
        k = 2
        result = top_k_frequent(nums, k)
        expected = [1, 2]  # 1:3 times, 2:2 times
        self.assertEqual(set(result), set(expected))
        self.assertEqual(len(result), k)
    

    def test_single_element(self):
        """Test with single element."""
        nums = [1]
        k = 1
        result = top_k_frequent(nums, k)
        self.assertEqual(result, [1])

    def test_all_same_frequency(self):
        """Test when all elements have same frequency."""
        nums = [1, 2, 3, 4]
        k = 2
        result = top_k_frequent(nums, k)
        # Any 2 elements are valid since all have freq=1
        self.assertEqual(len(result), k)
        self.assertTrue(all(x in nums for x in result))


    def test_k_equals_unique_count(self):
        """Test k equals number of unique elements."""
        nums = [1, 2, 3]
        k = 3
        result = top_k_frequent(nums, k)
        self.assertEqual(set(result), set(nums))
        self.assertEqual(len(result), k)


    def test_negative_numbers(self):
        """Test with negative numbers."""
        nums = [-1, -1, 2, 2, 3]
        k = 2
        result = top_k_frequent(nums, k)
        expected_set = {-1, 2}  # Both appear twice
        self.assertEqual(set(result), expected_set)
        self.assertEqual(len(result), k)


    def test_large_k(self):
        """Test with k close to array size."""
        nums = [1, 1, 2, 2, 3, 3, 4, 4, 5]
        k = 4
        result = top_k_frequent(nums, k)
        # Top 4 frequent: all except 5 (which appears once)
        expected_exclude = 5
        self.assertNotIn(expected_exclude, result)
        self.assertEqual(len(result), k)


    def test_duplicate_frequencies(self):
        """Test case with multiple elements having same frequency."""
        nums = [3, 0, 1, 0]
        k = 1
        result = top_k_frequent(nums, k)
        # 0 appears twice, others once - so 0 must be in result
        self.assertIn(0, result)

        self.assertEqual(len(result), 1)


    def test_empty_input(self):
        """Test empty input array."""
        nums = []
        k = 0
        result = top_k_frequent(nums, k)
        self.assertEqual(result, [])

if __name__ == "__main__":
    unittest.main()
