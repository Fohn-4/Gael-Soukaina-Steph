import os

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

def drop_piece(board, col, piece):
    # Parcourt les lignes du bas vers le haut pour trouver la première cellule vide
    for row in reversed(board):
        if row[col] == '⚫':  # Trouve la première cellule vide dans la colonne
            row[col] = piece
            return True
    return False  # Retourne False si la colonne est pleine

while run:
    cls()
    display_board(board)

    try:
        col = int(input(f"Player {currentPlayer}, choose a column (0-{cols-1}): "))
        if col < 0 or col >= cols:
            print("Invalid column. Please choose a column between 0 and 6.")
            continue
        if not drop_piece(board, col, currentPlayer):
            print("The column is full. Choose another one.")
            continue
        # Alterne les joueurs après une insertion réussie
        currentPlayer = yellowPlayer if currentPlayer == redPlayer else redPlayer
    except ValueError:
        print("Invalid input. Please enter a number.")

    keepGoing = input('''Continue? 
Y for yes
N for no
''')
    if keepGoing.upper() == 'N':
        run = False