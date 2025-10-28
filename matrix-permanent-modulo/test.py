import unittest
import sys
from io import StringIO
from solution import matrix_permanent, solve_matrix_permanent

class TestMatrixPermanent(unittest.TestCase):
    
    def test_small_matrices(self):
        matrix1 = [[1, 2], [3, 4]]
        self.assertEqual(matrix_permanent(matrix1, 2, 1000000007), 10)
        
        matrix2 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        self.assertEqual(matrix_permanent(matrix2, 3, 1000000007), 6)
    
    def test_identity_matrix(self):
        # Permanent of identity matrix is 1
        identity = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        self.assertEqual(matrix_permanent(identity, 3, 1000000007), 1)
    
    def test_zero_matrix(self):
        # Permanent of zero matrix is 0
        zero = [[0, 0], [0, 0]]
        self.assertEqual(matrix_permanent(zero, 2, 1000000007), 0)
    
    def test_permutation_matrix(self):
        # Matrix with one 1 in each row and column
        perm_matrix = [[0, 1, 0], [1, 0, 0], [0, 0, 1]]
        self.assertEqual(matrix_permanent(perm_matrix, 3, 1000000007), 1)
    
    def test_large_modulus(self):
        matrix = [[1, 2], [3, 4]]
        self.assertEqual(matrix_permanent(matrix, 2, 100), 10)
        self.assertEqual(matrix_permanent(matrix, 2, 5), 0)  # 10 mod 5 = 0
    
    def test_full_integration(self):
        input_data = """2
2 1000000007
1 2
3 4
3 1000000007
1 1 1
1 1 1
1 1 1"""
        
        expected_output = ["10", "6"]
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_matrix_permanent()
            self.assertEqual(results, expected_output)
        finally:
            sys.stdin = old_stdin

if __name__ == '__main__':
    unittest.main(verbosity=2)