import os
from check_winner import check_winner
from insert_jeton import drop_piece

cols = 7
rows = 6

run = True

yellowPlayer = '🟡'
redPlayer = '🔴'
currentPlayer = redPlayer  # The red player starts

board = [['⚫' for _ in range(cols)] for _ in range(rows)]

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_board(board):
    # Affiche chaque ligne du plateau
    for row in board:
        print(' '.join(row))
    print()  # Nouvelle ligne à la fin de l'affichage du plateau
    
while run:
    cls()
    display_board(board)

    try:
        col = int(input(f"Player {currentPlayer}, choose a column (1-{cols}): ")) - 1
        if col < 0 or col >= cols:
            print("Invalid column. Please choose a column between 1 and 7.")
            continue
        if not drop_piece(board, col, currentPlayer):
            print("The column is full. Choose another one.")
            continue
        # Vérifie si le joueur actuel a gagné après l'insertion
        if check_winner(board, currentPlayer):
            cls()
            display_board(board)
            print(f"Player {currentPlayer} wins!")
            break
        # Alterne les joueurs après une insertion réussie
        currentPlayer = yellowPlayer if currentPlayer == redPlayer else redPlayer
    except ValueError:
        print("Invalid input. Please enter a number.")
