import unittest
from solution import sliding_window_mode

class TestSlidingWindowMode(unittest.TestCase):
    
    def test_basic_case(self):
        nums = [4, 1, 1, 3, 3, 3]
        k = 3
        expected = [1, 1, 3, 3]
        self.assertEqual(sliding_window_mode(nums, k), expected)
    

    def test_k_equals_1(self):
        nums = [5, 2, 8]
        k = 1
        expected = [5, 2, 8]
        self.assertEqual(sliding_window_mode(nums, k), expected)

    def test_tie_in_frequency(self):
        nums = [2, 2, 1]
        k = 2
        expected = [2, 1]  # [2,2]->2; [2,1]->tie→min=1
        self.assertEqual(sliding_window_mode(nums, k), expected)

    def test_single_element_window(self):
        nums = [5, 5, 5]
        k = 1
        expected = [5, 5, 5]
        self.assertEqual(sliding_window_mode(nums, k), expected)

    def test_all_elements_same(self):
        nums = [3, 3, 3, 3]
        k = 2
        expected = [3, 3, 3]  # Every window has only 3s
        self.assertEqual(sliding_window_mode(nums, k), expected)

    def test_descending_order(self):
        nums = [5, 4, 3, 2, 1]
        k = 3
        # Windows: [5,4,3]→all freq=1→min=3; [4,3,2]→min=2; [3,2,1]→min=1
        expected = [3, 2, 1]
        self.assertEqual(sliding_window_mode(nums, k), expected)


    def test_ascending_order(self):
        nums = [1, 2, 3, 4, 5]
        k = 3
        # All windows have unique elements → return smallest in each
        expected = [1, 2, 3]
        self.assertEqual(sliding_window_mode(nums, k), expected)

    def test_large_k_equal_to_n(self):
        nums = [1, 2, 2, 3, 3, 3]
        k = len(nums)  # Single window
        # Frequencies: 1→1, 2→2, 3→3 → mode=3
        expected = [3]
        self.assertEqual(sliding_window_mode(nums, k), expected)


    def test_frequent_ties_with_smaller_wins(self):
        nums = [4, 4, 1, 1, 5, 5]  # Two pairs of freq=2
        k = 4
        # Window [4,4,1,1]: 4→2, 1→2 → tie → min=1
        # Window [4,1,1,5]: 1→2, others→1 → mode=1
        # Window [1,1,5,5]: 1→2, 5→2 → tie → min=1
        expected = [1, 1, 1]
        self.assertEqual(sliding_window_mode(nums, k), expected)


    def test_negative_numbers(self):
        nums = [-1, -1, -2, -2, -3]
        k = 3
        # [-1,-1,-2] → -1:2 → mode=-1
        # [-1,-2,-2] → -2:2 → mode=-2
        # [-2,-2,-3] → -2:2 → mode=-2
        expected = [-1, -2, -2]
        self.assertEqual(sliding_window_mode(nums, k), expected)


    def test_mixed_positive_negative(self):
        nums = [2, -2, 2, -2, 3]
        k = 3
        # [2,-2,2] → 2:2, -2:1 → mode=2
        # [-2,2,-2] → -2:2, 2:1 → mode=-2
        # [2,-2,3] → all:1 → min=-2
        expected = [2, -2, -2]
        self.assertEqual(sliding_window_mode(nums, k), expected)


    def test_long_sequence_with_repetition(self):
        nums = [1, 1, 2, 2, 1, 1, 3, 3, 3]
        k = 4
        # Manual verification:
        # [1,1,2,2] → 1:2, 2:2 → min=1
        # [1,2,2,1] → same → min=1
        # [2,2,1,1] → same → min=1
        # [2,1,1,3] → 1:2 → mode=1
        # [1,1,3,3] → 1:2, 3:2 → min=1
        # [1,3,3,3] → 3:3 → mode=3
        expected = [1, 1, 1, 1, 1, 3]
        self.assertEqual(sliding_window_mode(nums, k), expected)


    def test_edge_case_k_equals_len(self):
        nums = [7]
        k = 1
        expected = [7]
        self.assertEqual(sliding_window_mode(nums, k), expected)


    def test_performance_large_input(self):
        # Test with large input to verify O(n) behavior
        import random
        random.seed(42)
        nums = random.choices(range(1, 1001), k=10**4)
        k = 50
        result = sliding_window_mode(nums, k)
        self.assertEqual(len(result), len(nums) - k + 1)
        # Just test it runs without error and returns correct length


if __name__ == '__main__':
    unittest.main()
