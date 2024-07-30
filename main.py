


cols = 7
rows = 6

run = True

yellowPlayer = '🟡'
redPlayer = '🔴'

board = [['⚫' for _ in range(cols)] for _ in range(rows)]
    

while run:
    for row in board:
        print(row)

    keepGoing = input('''Continue ? 
                        Y for yes
                        N for no
                        ''')
    if keepGoing == 'Y':
        run = True
    elif keepGoing == 'N':
        run = False
    else:
        pass
    

