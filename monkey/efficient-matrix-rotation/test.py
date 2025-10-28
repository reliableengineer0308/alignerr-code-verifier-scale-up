import unittest
from solution import rotate_matrix



class TestRotateMatrix(unittest.TestCase):

    def test_1x1_matrix(self):
        """Test 1×1 matrix (no rotation needed)."""
        matrix = [[5]]
        rotate_matrix(matrix)
        self.assertEqual(matrix, [[5]])

    def test_2x2_matrix(self):
        """Test 2×2 matrix."""
        matrix = [
            [1, 2],
            [3, 4]
        ]
        # After 90° clockwise rotation:
        # 3 1
        # 4 2
        expected = [
            [3, 1],
            [4, 2]
        ]
        rotate_matrix(matrix)
        self.assertEqual(matrix, expected)

    def test_3x3_matrix(self):
        """Test 3×3 matrix."""
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        # After 90° clockwise rotation:
        # 7 4 1
        # 8 5 2
        # 9 6 3
        expected = [
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3]
        ]
        rotate_matrix(matrix)
        self.assertEqual(matrix, expected)

    def test_4x4_matrix(self):
        """Test 4×4 matrix."""
        matrix = [
            [5,  1,  9,  11],
            [2,  4,  8,  10],
            [13, 3,  6,  7 ],
            [15, 14, 12, 16]
        ]
        # After 90° clockwise rotation:
        # 15 13 2  5
        # 14 3  4  1
        # 12 6  8  9
        # 16 7  10 11
        expected = [
            [15, 13, 2,  5],
            [14, 3,  4,  1],
            [12, 6,  8,  9],
            [16, 7,  10, 11]
        ]
        rotate_matrix(matrix)
        self.assertEqual(matrix, expected)

    def test_odd_sized_matrix(self):
        """Test odd-sized matrix (5×5)."""
        matrix = [
            list(range(1, 6)),
            list(range(6, 11)),
            list(range(11, 16)),
            list(range(16, 21)),
            list(range(21, 26))
        ]
        expected = [
            [21, 16, 11, 6,  1],
            [22, 17, 12, 7,  2],
            [23, 18, 13, 8,  3],
            [24, 19, 14, 9,  4],
            [25, 20, 15, 10, 5]
        ]
        rotate_matrix(matrix)
        self.assertEqual(matrix, expected)

    def test_matrix_with_negative_numbers(self):
        """Test matrix containing negative numbers."""
        matrix = [
            [-1, -2],
            [-3, -4]
        ]
        # After rotation:
        # -3 -1
        # -4 -2
        expected = [
            [-3, -1],
            [-4, -2]
        ]
        rotate_matrix(matrix)
        self.assertEqual(matrix, expected)

    def test_matrix_with_duplicates(self):
        """Test matrix with duplicate values."""
        matrix = [
            [1, 1],
            [2, 2]
        ]
        # After rotation:
        # 2 1
        # 2 1
        expected = [
            [2, 1],
            [2, 1]
        ]
        rotate_matrix(matrix)
        self.assertEqual(matrix, expected)

    def test_identity_matrix(self):
        """Test identity matrix (n×n with 1s on diagonal)."""
        n = 4
        matrix = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
        expected = [[1 if i == (n-1-j) else 0 for j in range(n)] for i in range(n)]
        rotate_matrix(matrix)
        self.assertEqual(matrix, expected)


    def test_single_row_column(self):
        """Test edge case: technically 1×n or n×1 (though problem states n×n)."""
        # Since problem specifies square matrix, we test 1×1 already
        # This is just to ensure no index errors on minimal case
        matrix = [[42]]
        rotate_matrix(matrix)
        self.assertEqual(matrix, [[42]])


    def test_large_matrix_performance(self):
        """Stress test with larger matrix (10×10) to check for index errors."""
        n = 10
        matrix = [[i * n + j for j in range(n)] for i in range(n)]
        # Create expected manually by rotating
        expected = [[matrix[n-1-j][i] for j in range(n)] for i in range(n)]
        rotate_matrix(matrix)
        self.assertEqual(matrix, expected)


    def test_in_place_modification(self):
        """Verify that the function modifies the matrix in-place (no new object created)."""
        original_matrix = [
            [1, 2],
            [3, 4]
        ]
        # Capture the original object id
        original_id = id(original_matrix)
        
        rotate_matrix(original_matrix)
        # Check that the object identity hasn't changed
        self.assertEqual(id(original_matrix), original_id)
        # And values are correctly rotated
        self.assertEqual(original_matrix, [[3, 1], [4, 2]])



if __name__ == '__main__':
    unittest.main()
