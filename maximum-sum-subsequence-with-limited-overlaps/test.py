import unittest
from solution import maxSumSubsequence

class TestMaxSumSubsequence(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual(maxSumSubsequence([3, -2, 5, -1], 2), 8)

    def test_k_equals_1(self):
        # k=1: can't pick adjacent indices, but can pick non-adjacent ones
        # nums = [1, 2, 3, 4]
        # Best: pick indices 1 and 3 → 2 + 4 = 6
        self.assertEqual(maxSumSubsequence([1, 2, 3, 4], 1), 6)

    def test_peak_valley(self):
        # nums = [1, 5, 2, 8, 3], k=2
        # Valid picks: indices 0,1,3,4 → values 1+5+8+3 = 17
        # Consecutive runs: 0-1 (2), then gap, then 3-4 (2) → both ≤k=2
        self.assertEqual(maxSumSubsequence([1, 5, 2, 8, 3], 2), 17)


    def test_all_negative(self):
        self.assertEqual(maxSumSubsequence([-1, -2, -3], 3), 0)


    def test_four_elements_k3(self):
        self.assertEqual(maxSumSubsequence([2, 1, 3, 4, 5], 3), 14)


    def test_repeated_values(self):
        self.assertEqual(maxSumSubsequence([5, 5, 5, 5], 2), 15)


    def test_single_element(self):
        self.assertEqual(maxSumSubsequence([7], 1), 7)

    def test_large_k(self):
        # k = len(nums), so we can pick all elements (no restriction on consecutive picks)
        nums = [1, -1, 2, -2, 3]
        k = len(nums)  # k = 5, no effective limit
        # We can pick all positive numbers: 1 + 2 + 3 = 6
        self.assertEqual(maxSumSubsequence(nums, k), 6)

    def test_k_equals_length(self):
        # When k equals array length, we can pick any subsequence (no consecutive limit)
        # So it's equivalent to "pick all positive numbers"
        nums = [-5, 10, -3, 8, -1]
        k = len(nums)
        expected = 10 + 8  # Only positive numbers
        self.assertEqual(maxSumSubsequence(nums, k), expected)

    def test_all_positive(self):
        # All positive: should pick as many as possible, respecting k
        nums = [2, 3, 1, 4, 5]
        k = 2
        # Best: pick indices 0,1 (sum=5) and 3,4 (sum=9) → total=14
        # Or 0,2,3,4 → 2+1+4+5=12 → worse
        # Actually: 0,1 and 3,4 = 2+3+4+5 = 14
        self.assertEqual(maxSumSubsequence(nums, k), 14)

    def test_alternating_signs(self):
        nums = [5, -3, 4, -2, 6]
        k = 2
        # Best: 5 (index0), skip index1, pick 4 (index2), skip index3, pick 6 (index4)
        # Sum = 5 + 4 + 6 = 15
        # Can we do better? Try 5,-3,4 → invalid (3 consecutive). 
        # 5,4,6 → not consecutive indices → valid → sum=15
        self.assertEqual(maxSumSubsequence(nums, k), 15)

    def test_max_consecutive_run(self):
        nums = [10, 20, 30, -5, 40]
        k = 3
        # Best: pick first 3 → 10+20+30 = 60 (exactly k=3 consecutive)
        # Then skip -5, pick 40 → total = 60 + 40 = 100
        # But indices 0-2 are consecutive → allowed. Index 4 is separate.
        self.assertEqual(maxSumSubsequence(nums, k), 100)

    def test_negative_in_middle(self):
        nums = [4, 5, -10, 6, 7]
        k = 2
        # Avoid -10. Best: pick 4,5 (sum=9, consecutive → allowed) then skip -10, pick 6,7 (sum=13)
        # Total = 9 + 13 = 22
        # But 4,5 are indices 0-1 (k=2 allowed), 6,7 are indices 3-4 (k=2 allowed)
        self.assertEqual(maxSumSubsequence(nums, k), 22)

    def test_single_negative(self):
        nums = [-10]
        k = 1
        # Only one element, negative → best to pick nothing → sum=0
        self.assertEqual(maxSumSubsequence(nums, k), 0)

    def test_two_elements_k1(self):
        nums = [3, 4]
        k = 1
        # Can't pick both (adjacent). Best: pick 4 → sum=4
        self.assertEqual(maxSumSubsequence(nums, k), 4)


if __name__ == '__main__':
    unittest.main()

