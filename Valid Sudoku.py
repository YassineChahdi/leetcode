
def ValidSudoku(board):
    # Check valid row
    for i in range(9):
        digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        for j in range(9):
            if board[i][j] in digits:
                digits.remove(board[i][j])
            elif board[i][j] == ".":
                continue
            else:
                return False
    # Check valid column
    for i in range(9):
        digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        for j in range(9):
            if board[j][i] in digits:
                digits.remove(board[j][i])
            elif board[j][i] == ".":
                continue
            else:
                return False
    # Check valid square
    for i in range(3):
        for j in range(3):
            digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
            for k in range(3):
                for l in range(3):
                    if board[k + (3 * i)][l + (3 * j)] in digits:
                        digits.remove(board[k + (3 * i)][l + (3 * j)])
                    elif board[k + (3 * i)][l + (3 * j)] == ".":
                        continue
                    else:
                        return False
    return True
