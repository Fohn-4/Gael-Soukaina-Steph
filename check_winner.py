def check_winner(board, player):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == player:
                # Check horizontal
                if col + 3 < len(board[0]) and all(board[row][c] == player for c in range(col, col + 4)):
                    return True
                # Check vertical
                if row + 3 < len(board) and all(board[r][col] == player for r in range(row, row + 4)):
                    return True
                # Check diagonals
                if col + 3 < len(board[0]):
                    if row + 3 < len(board) and all(board[row + i][col + i] == player for i in range(4)):
                        return True
                    if row - 3 >= 0 and all(board[row - i][col + i] == player for i in range(4)):
                        return True
    print("blop")
    return False