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

