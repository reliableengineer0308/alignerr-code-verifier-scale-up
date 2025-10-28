import unittest
from solution import numDistinctIslands

class TestNumDistinctIslands(unittest.TestCase):
    def test_example_1_same_shapes(self):
        grid = [
            [1,1,0,0,0],
            [1,1,0,0,0],
            [0,0,0,1,1],
            [0,0,0,1,1]
        ]
        result = numDistinctIslands(grid)
        self.assertEqual(result, 1)  # Both are 2x2 squares

    def test_example_2_three_distinct(self):
        grid = [
            [1,1,0,1,1],
            [1,0,0,0,0],
            [0,0,0,0,1],
            [1,1,0,1,1]
        ]
        result = numDistinctIslands(grid)
        self.assertEqual(result, 3)  # Three unique shapes

    def test_single_cell(self):
        grid = [[1]]
        result = numDistinctIslands(grid)
        self.assertEqual(result, 1)

    def test_no_land(self):
        grid = [[0,0],[0,0]]
        result = numDistinctIslands(grid)
        self.assertEqual(result, 0)

    def test_disconnected_same_shape(self):
        grid = [
            [1,0],
            [0,1]
        ]  # Two single-cell islands → same shape
        result = numDistinctIslands(grid)
        self.assertEqual(result, 1)

    def test_l_shaped_islands(self):
        grid = [
            [1,1,0],
            [1,0,0],
            [0,0,1],
            [0,1,1]
        ]
        # First: L-shape (3 cells), Second: 2-cell line → two distinct
        result = numDistinctIslands(grid)
        self.assertEqual(result, 2)

    def test_vertical_horizontal_lines(self):
        grid = [
            [1, 0, 0],
            [1, 0, 0],
            [1, 0, 1],
            [0, 0, 1],
            [0, 0, 1]
        ]
        # Island 1: vertical line of 3 cells (col 0)
        # Island 2: vertical line of 3 cells (col 2, rows 2-4)
        # Same shape (vertical line of length 3) → count as 1 distinct shape
        result = numDistinctIslands(grid)
        self.assertEqual(result, 1)

    def test_complex_mixed_shapes(self):
        grid = [
            [1, 1, 0, 0, 1],
            [1, 0, 0, 1, 1],
            [0, 0, 1, 1, 0],
            [0, 1, 1, 0, 0]
        ]

        result = numDistinctIslands(grid)
        self.assertEqual(result, 2)

    def test_diagonal_islands(self):
        grid = [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]
        ]
        # Three single-cell islands → same shape (single point)
        result = numDistinctIslands(grid)
        self.assertEqual(result, 1)

    def test_large_connected_island(self):
        grid = [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]
        ]
        # One 3x3 square island → only one shape
        result = numDistinctIslands(grid)
        self.assertEqual(result, 1)

if __name__ == "__main__":
    unittest.main()
