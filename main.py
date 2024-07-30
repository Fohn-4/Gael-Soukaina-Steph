
from check_winner import *

import os


cols = 7
rows = 6

run = True

yellowPlayer = '🟡'
redPlayer = '🔴'

board = [['⚫' for _ in range(cols)] for _ in range(rows)]
    
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

while run:
    cls()

    for row in board:
        print(row)

    keepGoing = input('''Continue ? 
                        Y for yes
                        N for no
                        ''')
    if keepGoing.upper() == 'N':
        run = False

    

