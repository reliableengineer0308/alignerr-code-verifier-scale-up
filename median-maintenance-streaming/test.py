import unittest
from solution import median_maintenance

class TestMedianMaintenance(unittest.TestCase):
    
    def test_single_element(self):
        """Single element → median is itself."""
        self.assertEqual(median_maintenance([5]), [5])
    
    def test_two_elements(self):
        """Two elements → average (floor division)."""
        self.assertEqual(median_maintenance([1, 2]), [1, 1])  # (1+2)//2 = 1
    
    def test_three_elements(self):
        """Three elements → middle one."""
        self.assertEqual(median_maintenance([3, 1, 2]), [3, 2, 2])
    
    def test_increasing_sequence(self):
        """Increasing numbers."""
        self.assertEqual(
            median_maintenance([1, 2, 3, 4, 5]),
            [1, 1, 2, 2, 3]
        )
    def test_decreasing_sequence(self):
        """Decreasing numbers."""
        self.assertEqual(
            median_maintenance([5, 4, 3, 2, 1]),
            [5, 4, 4, 3, 3]
        )
    def test_with_duplicates(self):
        """Stream with repeated values."""
        self.assertEqual(
            median_maintenance([2, 2, 1, 3]),
            [2, 2, 2, 2]
        )
    def test_mixed_signs(self):
        """Positive and negative numbers."""
        self.assertEqual(
            median_maintenance([-1, 0, 1]),
            [-1, -1, 0]
        )
    def test_large_numbers(self):
        """Large values."""
        self.assertEqual(
            median_maintenance([100000, -100000]),
            [100000, 0]  # (100000 + (-100000))//2 = 0
        )

if __name__ == '__main__':
    unittest.main()
