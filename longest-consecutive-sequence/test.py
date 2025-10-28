import unittest
from solution import longest_consecutive

class TestLongestConsecutive(unittest.TestCase):
    """Unit tests for longest_consecutive function."""

    def test_example_1(self):
        """Test: [100,4,200,1,3,2] → longest sequence [1,2,3,4] → length 4"""
        self.assertEqual(longest_consecutive([100, 4, 200, 1, 3, 2]), 4)

    def test_example_2(self):
        """Test: [0,3,7,2,5,8,4,6,0,1] → [0,1,2,3,4,5,6,7,8] → length 9"""
        self.assertEqual(longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]), 9)

    def test_example_3(self):
        """Empty array → 0"""
        self.assertEqual(longest_consecutive([]), 0)

    def test_example_4(self):
        """Single element → 1"""
        self.assertEqual(longest_consecutive([7]), 1)

    def test_example_5(self):
        """Duplicates: [1,2,0,1] → sequence [0,1,2] → length 3"""
        self.assertEqual(longest_consecutive([1, 2, 0, 1]), 3)

    def test_all_same_elements(self):
        """All duplicates: [5,5,5] → sequence length 1"""
        self.assertEqual(longest_consecutive([5, 5, 5]), 1)

    def test_negative_numbers(self):
        """Negatives: [-2,-1,0,1] → full sequence → length 4"""
        self.assertEqual(longest_consecutive([-2, -1, 0, 1]), 4)

    def test_mixed_negatives_and_positives(self):
        """[-3,-2,1,2,3] → two sequences: [-3,-2] and [1,2,3] → max 3"""
        self.assertEqual(longest_consecutive([-3, -2, 1, 2, 3]), 3)

    def test_no_consecutive(self):
        """No consecutive numbers: 10, 20, 30 → each is isolated → max length 1"""
        self.assertEqual(longest_consecutive([10, 20, 30]), 1)

    def test_already_sorted_consecutive(self):
        """Already sorted and consecutive: 1,2,3,4,5 → length 5"""
        self.assertEqual(longest_consecutive([1, 2, 3, 4, 5]), 5)

    def test_reverse_sorted_consecutive(self):
        """Reverse sorted: 5,4,3,2,1 → still forms sequence 1..5 → length 5"""
        self.assertEqual(longest_consecutive([5, 4, 3, 2, 1]), 5)

    def test_scattered_with_one_long_sequence(self):
        """Scattered nums with one long sequence: 100, 4, 200, 1, 3, 2, 50, 51 → longest is 1..4 → length 4"""
        self.assertEqual(longest_consecutive([100, 4, 200, 1, 3, 2, 50, 51]), 4)

    def test_multiple_sequences_same_length(self):
        """Two sequences of same length: 1,2 and 10,11 → both length 2 → return 2"""
        self.assertEqual(longest_consecutive([1, 2, 10, 11]), 2)

    def test_sequence_with_gaps(self):
        """Numbers with gaps: 1,3,5,7 → no consecutive pairs → max length 1"""
        self.assertEqual(longest_consecutive([1, 3, 5, 7]), 1)

    def test_large_numbers(self):
        """Large integers: 1e9, 1e9+1, 1e9+2 → valid consecutive sequence → length 3"""
        nums = [10**9, 10**9 + 1, 10**9 + 2]
        self.assertEqual(longest_consecutive(nums), 3)

    def test_negative_large_sequence(self):
        """Negative large sequence: -5,-4,-3,-2,-1 → length 5"""
        self.assertEqual(longest_consecutive([-5, -4, -3, -2, -1]), 5)

    def test_single_pair(self):
        """Only one consecutive pair: 1,3,4,6 → 3,4 is the only sequence → length 2"""
        self.assertEqual(longest_consecutive([1, 3, 4, 6]), 2)

    def test_all_negatives_no_sequence(self):
        """All negatives, no sequence: -10,-5,-1 → each isolated → length 1"""
        self.assertEqual(longest_consecutive([-10, -5, -1]), 1)

    def test_huge_input_random(self):
        """Stress test: 10k random integers → verify it runs in O(n)"""
        import random
        # Generate 10k random ints in range -1e5 to 1e5
        nums = [random.randint(-100000, 100000) for _ in range(10000)]
        result = longest_consecutive(nums)
        # Just verify it returns valid int >= 1 (unless empty)
        self.assertIsInstance(result, int)
        if nums:
            self.assertGreaterEqual(result, 1)
        else:
            self.assertEqual(result, 0)

    def test_edge_case_single_zero(self):
        """Single zero → length 1"""
        self.assertEqual(longest_consecutive([0]), 1)

    def test_zero_and_neighbors(self):
        """0, -1, 1 → forms -1,0,1 → length 3"""
        self.assertEqual(longest_consecutive([0, -1, 1]), 3)

    def test_duplicates_with_sequence(self):
        """Duplicates within sequence: 0,0,1,1,2,2 → sequence 0,1,2 → length 3"""
        self.assertEqual(longest_consecutive([0, 0, 1, 1, 2, 2]), 3)

    def test_long_sequence_in_middle(self):
        """Long sequence not at edges: 10,11,12, 0,1,2,3,4 → longest is 0..4 → length 5"""
        self.assertEqual(longest_consecutive([10, 11, 12, 0, 1, 2, 3, 4]), 5)

    def test_two_separate_long_sequences(self):
        """Two long sequences: 1..5 and 10..14 → both length 5 → return 5"""
        nums = list(range(1, 6)) + list(range(10, 15))
        self.assertEqual(longest_consecutive(nums), 5)


    def test_alternating_signs_with_sequence(self):
        """Alternating signs but forming sequence: -2, -1, 0, 1, 2 → length 5"""
        self.assertEqual(longest_consecutive([-2, -1, 0, 1, 2]), 5)

if __name__ == '__main__':
    unittest.main()
