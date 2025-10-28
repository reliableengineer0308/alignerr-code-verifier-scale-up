def is_valid_sudoku(board):
    # Check rows
    for i in range(9):
        seen = set()
        for j in range(9):
            if board[i][j] != '.':
                if board[i][j] in seen:
                    return False
                seen.add(board[i][j])
    
    # Check columns
    for j in range(9):
        seen = set()
        for i in range(9):
            if board[i][j] != '.':
                if board[i][j] in seen:
                    return False
                seen.add(board[i][j])
    
    # Check 3x3 sub-boxes
    for box_i in range(3):
        for box_j in range(3):
            seen = set()
            for i in range(3 * box_i, 3 * box_i + 3):
                for j in range(3 * box_j, 3 * box_j + 3):
                    if board[i][j] != '.':
                        if board[i][j] in seen:
                            return False
                        seen.add(board[i][j])
    
    return True