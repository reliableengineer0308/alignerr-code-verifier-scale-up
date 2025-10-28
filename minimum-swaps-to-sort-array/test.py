import unittest
from solution import minimum_swaps_to_sort

class TestMinimumSwapsToSort(unittest.TestCase):
    
    def test_already_sorted(self):
        """Test arrays that are already in ascending order."""
        self.assertEqual(minimum_swaps_to_sort([1, 2, 3]), 0)
        self.assertEqual(minimum_swaps_to_sort([5]), 0)  # Single element
        self.assertEqual(minimum_swaps_to_sort([]), 0)   # Empty array


    def test_two_elements(self):
        """Test minimal case with two elements."""
        self.assertEqual(minimum_swaps_to_sort([2, 1]), 1)  # Needs one swap
        self.assertEqual(minimum_swaps_to_sort([1, 2]), 0)  # Already sorted


    def test_example_1(self):
        """Test case: [4, 3, 2, 1] -> 2 swaps."""
        # Cycle 1: 4 → 1 → 4 (length 2) → requires 1 swap
        # Cycle 2: 3 → 2 → 3 (length 2) → requires 1 swap
        # Total swaps: 2
        self.assertEqual(minimum_swaps_to_sort([4, 3, 2, 1]), 2)

    def test_example_2(self):
        """Test case: [1, 5, 4, 3, 2] -> 2 swaps."""
        # Cycles:
        # - 1 is already in correct position
        # - 5 → 2 → 5 (cycle length 2) → 1 swap needed
        # - 4 → 3 → 4 (cycle length 2) → 1 swap needed
        # Total: 2 swaps
        self.assertEqual(minimum_swaps_to_sort([1, 5, 4, 3, 2]), 2)

    def test_reverse_sorted(self):
        """Test reverse-sorted array: [5, 4, 3, 2, 1] -> 2 swaps."""
        arr = [5, 4, 3, 2, 1]
        # Cycles:
        # - (5 → 1 → 5): cycle length 2 → 1 swap
        # - (4 → 2 → 4): cycle length 2 → 1 swap  
        # - 3 is already in correct position
        # Total: 2 swaps
        self.assertEqual(minimum_swaps_to_sort(arr), 2)

    def test_single_cycle(self):
        """Test a single cycle of length 4: [2, 3, 4, 1] -> 3 swaps."""
        arr = [2, 3, 4, 1]  # Element 1 should be at index 3 but is at 0
        # Full cycle: 2 → 3 → 4 → 1 → 2 (length 4)
        # Swaps needed: cycle_length - 1 = 4 - 1 = 3
        self.assertEqual(minimum_swaps_to_sort(arr), 3)

    def test_large_array(self):
        """Test performance on a larger shuffled array (n=100)."""
        import random
        arr = list(range(100))
        random.shuffle(arr)
        result = minimum_swaps_to_sort(arr)
        
        # Minimum possible swaps is 0 (if already sorted)
        self.assertGreaterEqual(result, 0)
        # Maximum possible swaps for n elements is n-1 (single cycle)
        self.assertLessEqual(result, len(arr) - 1)

    def test_edge_cases(self):
        """Test various edge cases including empty, single, and mixed-sign arrays."""
        # Empty array
        self.assertEqual(minimum_swaps_to_sort([]), 0)
        
        # Single element
        self.assertEqual(minimum_swaps_to_sort([42]), 0)
        
        # Two elements (already sorted)
        self.assertEqual(minimum_swaps_to_sort([10, 20]), 0)
        
        # Two elements (need swap)
        self.assertEqual(minimum_swaps_to_sort([100, 50]), 1)
        
        # Three elements: full cycle (1→2→3→1)
        # Array: [2, 3, 1] → cycles: 2→3→1→2 (length 3) → swaps = 2
        self.assertEqual(minimum_swaps_to_sort([2, 3, 1]), 2)
        
        # Three elements: one fixed, two in cycle
        # Array: [1, 3, 2] → cycle: 3→2→3 (length 2) → swaps = 1
        self.assertEqual(minimum_swaps_to_sort([1, 3, 2]), 1)
        
        # Large negative numbers
        self.assertEqual(minimum_swaps_to_sort([-5, -10, -1]), 1)  # Swap -5 and -10
        
        # Mixed positive and negative values
        # Array: [3, -1, 0, 2] 
        # Sorted: [-1, 0, 2, 3]
        # Cycle: -1→0→2→3→-1? Actually: 
        # Index 0: 3 should go to index 3 → go to 3
        # Index 3: 2 should go to index 2 → go to 2  
        # Index 2: 0 should go to index 1 → go to 1
        # Index 1: -1 should go to index 0 → cycle closes
        # Final cycle: 0→3→2→1→0 (length 4) → swaps = 3
        self.assertEqual(minimum_swaps_to_sort([3, -1, 0, 2]), 3)


    def test_duplicate_values_handling(self):
        """
        Test that the function doesn't crash on duplicate values 
        (though the problem states all elements are distinct).
        This is a robustness check only — correctness isn't guaranteed for duplicates.
        """
        try:
            result = minimum_swaps_to_sort([1, 1, 2])
            # Just verify no exception was raised
            self.assertTrue(isinstance(result, int))
        except Exception as e:
            self.fail(f"Function raised exception on duplicate values: {e}")


if __name__ == '__main__':
    unittest.main()
