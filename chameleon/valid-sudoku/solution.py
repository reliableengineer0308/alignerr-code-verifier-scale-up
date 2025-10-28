def is_valid_sudoku(board):
    """
    Checks if a 9x9 Sudoku board is valid based on filled cells.
    Time: O(1) [fixed 9x9], Space: O(1) [9 sets max]
    """
    # Initialize sets for rows, cols, boxes
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]  # box_id = (r//3)*3 + (c//3)


    for r in range(9):
        for c in range(9):
            cell = board[r][c]
            if cell == '.':
                continue  # Skip empty cells

            # Check row
            if cell in rows[r]:
                return False
            rows[r].add(cell)


            # Check column
            if cell in cols[c]:
                return False
            cols[c].add(cell)

            
            # Check 3x3 box
            box_id = (r // 3) * 3 + (c // 3)
            if cell in boxes[box_id]:
                return False
            boxes[box_id].add(cell)


    return True
