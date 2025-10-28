import unittest
from solution import longestIncreasingPath

class TestLongestIncreasingPath(unittest.TestCase):
    def test_example_1(self):
        matrix = [
            [9, 9, 4],
            [6, 6, 8],
            [2, 1, 1]
        ]
        result = longestIncreasingPath(matrix)
        self.assertEqual(result, 4)  # Path: 1 → 2 → 6 → 9

    def test_example_2(self):
        matrix = [
            [3, 4, 5],
            [3, 2, 6],
            [2, 2, 1]
        ]
        result = longestIncreasingPath(matrix)
        self.assertEqual(result, 4)  # 3 → 4 → 5 → 6

    def test_single_cell(self):
        matrix = [[5]]
        result = longestIncreasingPath(matrix)
        self.assertEqual(result, 1)

    def test_flat_matrix(self):
        matrix = [[1, 1], [1, 1]]
        result = longestIncreasingPath(matrix)
        self.assertEqual(result, 1)  # No strictly increasing moves

    def test_strictly_increasing_row(self):
        matrix = [[1, 2, 3, 4]]
        result = longestIncreasingPath(matrix)
        self.assertEqual(result, 4)

    def test_diagonal_increasing(self):
        matrix = [
            [1, 3],
            [2, 4]
        ]
        result = longestIncreasingPath(matrix)
        self.assertEqual(result, 3)  # e.g., 1 → 3 → 4

    def test_negative_values(self):
        matrix = [
            [-5, -3],
            [-4, -2]
        ]
        result = longestIncreasingPath(matrix)
        self.assertEqual(result, 3)  # -5 → -4 → -2 OR -5 → -3 → -2

    def test_small_increasing_spiral(self):
        # A matrix where a clear 5-length path exists
        matrix = [
            [1, 2, 3],
            [8, 9, 4],
            [7, 6, 5]
        ]
        # Path: 1→2→3→4→5→6→7→8→9 → length = 9
        result = longestIncreasingPath(matrix)
        self.assertEqual(result, 9)

if __name__ == "__main__":
    unittest.main()
