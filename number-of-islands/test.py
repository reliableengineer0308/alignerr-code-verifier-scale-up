import unittest
from solution import num_islands

class TestNumIslands(unittest.TestCase):

    def test_single_island(self):
        """Test with one large connected island."""
        grid = [
            ['1','1','1','1','0'],
            ['1','1','0','1','0'],
            ['1','1','0','0','0'],
            ['0','0','0','0','0']
        ]
        self.assertEqual(num_islands(grid), 1)

    def test_three_islands(self):
        """Test with three separate islands."""
        grid = [
            ['1','1','0','0','0'],
            ['1','1','0','0','0'],
            ['0','0','1','0','0'],
            ['0','0','0','1','1']
        ]
        self.assertEqual(num_islands(grid), 3)

    def test_no_islands(self):
        """Test grid with no land (all water)."""
        grid = [
            ['0','0','0'],
            ['0','0','0'],
            ['0','0','0']
        ]
        self.assertEqual(num_islands(grid), 0)

    def test_all_land(self):
        """Test grid where all cells are land."""
        grid = [
            ['1','1','1'],
            ['1','1','1'],
            ['1','1','1']
        ]
        self.assertEqual(num_islands(grid), 1)

    def test_single_cell_land(self):
        """Test 1x1 grid with land."""
        grid = [['1']]
        self.assertEqual(num_islands(grid), 1)

    def test_single_cell_water(self):
        """Test 1x1 grid with water."""
        grid = [['0']]
        self.assertEqual(num_islands(grid), 0)

    def test_diagonal_islands(self):
        """Test islands separated diagonally (not connected)."""
        grid = [
            ['1','0','1'],
            ['0','1','0'],
            ['1','0','1']
        ]
        # Each '1' is isolated (no horizontal/vertical connection)
        self.assertEqual(num_islands(grid), 5)

    def test_empty_grid(self):
        """Test empty grid."""
        grid = []
        self.assertEqual(num_islands(grid), 0)

if __name__ == "__main__":
    unittest.main()
