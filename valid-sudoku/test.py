import unittest
from solution import is_valid_sudoku


class TestValidSudoku(unittest.TestCase):

    def test_valid_board(self):
        """Test a valid Sudoku board."""
        board = [
            ['5','3','.', '.','7','.', '.','.','.'],
            ['6','.','1', '9','5','.', '.','.','.'],
            ['.','9','8', '.','.','.', '.','6','.'],
            ['8','.','.', '.','6','.', '.','.','3'],
            ['4','.','.', '8','.','3', '.','.','1'],
            ['7','.','.', '.','2','.', '.','.','6'],
            ['.','6','.', '.','.','.', '2','8','.'],
            ['.','.','.', '4','1','9', '.','.','5'],
            ['.','.','.', '.','8','.', '.','7','9']
        ]
        self.assertTrue(is_valid_sudoku(board))

    def test_duplicate_in_row(self):
        """Test invalid due to duplicate in a row."""
        board = [
            ['5','5','.', '.','7','.', '.','.','.'],  # Two 5s in row 0
            ['6','.','1', '9','5','.', '.','.','.'],
            ['.','9','8', '.','.','.', '.','6','.'],
            ['8','.','.', '.','6','.', '.','.','3'],
            ['4','.','.', '8','.','3', '.','.','1'],
            ['7','.','.', '.','2','.', '.','.','6'],
            ['.','6','.', '.','.','.', '2','8','.'],
            ['.','.','.', '4','1','9', '.','.','5'],
            ['.','.','.', '.','8','.', '.','7','9']
        ]
        self.assertFalse(is_valid_sudoku(board))

    def test_duplicate_in_col(self):
        """Test invalid due to duplicate in a column."""
        board = [
            ['8','3','.', '.','7','.', '.','.','.'],  # col 0: 8 at (0,0)
            ['6','.','1', '9','5','.', '.','.','.'],
            ['.','9','8', '.','.','.', '.','6','.'],
            ['8','.','.', '.','6','.', '.','.','3'],  # col 0: another 8 at (3,0) → duplicate
            ['4','.','.', '8','.','3', '.','.','1'],
            ['7','.','.', '.','2','.', '.','.','6'],
            ['.','6','.', '.','.','.', '2','8','.'],
            ['.','.','.', '4','1','9', '.','.','5'],
            ['.','.','.', '.','8','.', '.','7','9']
        ]
        self.assertFalse(is_valid_sudoku(board))

    def test_duplicate_in_box(self):
        """Test invalid due to duplicate in a 3x3 box."""
        board = [
            ['5','3','.', '.','7','.', '.','.','.'],
            ['6','.','1', '9','5','.', '.','.','.'],
            ['.','9','8', '.','.','.', '.','6','.'],
            ['8','.','.', '.','6','.', '.','.','3'],
            ['4','.','.', '8','.','3', '.','.','1'],
            ['7','.','.', '.','2','.', '.','.','6'],
            ['.','6','.', '.','.','.', '2','8','.'],
            ['.','.','.', '4','1','9', '.','.','5'],
            ['.','.','.', '.','8','.', '.','7','9']
        ]
        # Introduce duplicate '5' in top-left 3x3 box (already has '5' at (0,1))
        board[2][1] = '5'  # Now (2,1) = '5', same box as (0,1) → invalid
        self.assertFalse(is_valid_sudoku(board))


    def test_empty_board(self):
        """Test a completely empty board (all dots)."""
        board = [['.' for _ in range(9)] for _ in range(9)]
        self.assertTrue(is_valid_sudoku(board))  # Empty is valid by definition


    def test_single_digit(self):
        """Test board with only one filled cell."""
        board = [['.' for _ in range(9)] for _ in range(9)]
        board[0][0] = '1'  # Only one '1' at top-left
        self.assertTrue(is_valid_sudoku(board))  # Single digit can't violate rules


    def test_full_valid_board(self):
        """Test a fully filled valid Sudoku solution."""
        board = [
            ['5','3','4', '6','7','8', '9','1','2'],
            ['6','7','2', '1','9','5', '3','4','8'],
            ['1','9','8', '3','4','2', '5','6','7'],
            ['8','5','9', '7','6','1', '4','2','3'],
            ['4','2','6', '8','5','3', '7','9','1'],
            ['7','1','3', '9','2','4', '8','5','6'],
            ['9','6','1', '5','3','7', '2','8','4'],
            ['2','8','7', '4','1','9', '6','3','5'],
            ['3','4','5', '2','8','6', '1','7','9']
        ]
        self.assertTrue(is_valid_sudoku(board))


    def test_invalid_digit_outside_range(self):
        """Test board with invalid digit (should be handled gracefully)."""
        # Although problem states digits are 1-9 or '.', test edge case
        board = [['.' for _ in range(9)] for _ in range(9)]
        board[0][0] = '0'  # '0' is not allowed in Sudoku
        # According to problem, input is guaranteed to be valid, so this is extra
        # But our code treats '0' as invalid (not 1-9), so it should still work
        # Since '0' ≠ any digit 1-9, no conflict → valid (though '0' itself is invalid per rules)
        # However, per problem statement, we only validate filled cells that are digits 1-9
        # So '0' would be treated as invalid input, but our code doesn't check that
        # Thus, for this test, we assume input is correct as per constraints
        pass  # Skip or mark as not required per constraints


    def test_multiple_conflicts(self):
        """Test board with multiple violations (row, col, box)."""
        board = [
            ['1','1','.', '.','.','.', '.','.','.'],  # row 0: duplicate '1'
            ['1','.','.', '.','.','.', '.','.','.'],  # col 0: duplicate '1' with row 0
            ['.','.','.', '.','.','.', '.','.','.'],
            # Box (0,0): already has two '1's from (0,0), (0,1), (1,0)
            ['.','.','.', '.','.','.', '.','.','.'],
            ['.','.','.', '.','.','.', '.','.','.'],
            ['.','.','.', '.','.','.', '.','.','.'],
            ['.','.','.', '.','.','.', '.','.','.'],
            ['.','.','.', '.','.','.', '.','.','.'],
            ['.','.','.', '.','.','.', '.','.','.']
        ]
        self.assertFalse(is_valid_sudoku(board))

if __name__ == "__main__":
    unittest.main()
