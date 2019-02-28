def create_board():
    board = []
    for _ in range(6):
        board.append(['•' for _ in range(7)])

    return board

def print_board(board):
    for row in board:
        for spot in row:
            print(spot, end = " ")
        print()

def valid_move(cmd, column_tally):
    if cmd not in column_tally or column_tally[cmd] < 6:
        return True

    print('That column is filled up!')
    return False

def find_row(n):
    ref = {0:5, 1:4, 2:3, 3:2, 4:1, 5:0}

    return ref[n]

def check_row(board,p1_p2,row):
    check_for = '☆'
    max_count = 0
    cur_count = 0
    cur_row = board[row]
    
    print('checking row')
    print(cur_row)

    if p1_p2:
        check_for = '★'

    for i in range(len(cur_row)):
        if cur_row[i] == check_for:
            j = i
            while j < len(cur_row):
                if cur_row[j] == check_for:
                    cur_count += 1
                    max_count = max(cur_count, max_count)
                    if max_count == 4:
                       break
                    j += 1
                else:
                    break
        cur_count = 0
    
    print(max_count)
    if max_count == 4:
        return True
    else:
        return False

def check_winner(board, cmd, p1_p2, column_tally):
    print(column_tally)
    row = column_tally[cmd] - 1
    row = find_row(row)
    print('row: ', end="")
    print(row)

    if check_row(board, p1_p2, row):
        return True
    return False

def place_piece(board, cmd, p1_p2, column_tally):
    col_num = int(cmd) - 1
    row_num = None

    if cmd in column_tally:
        row_num = column_tally[cmd]
        column_tally[cmd] += 1 
    else:
        row_num = 0
        column_tally[cmd] = 1

    row_num = find_row(row_num)

    if p1_p2:
        board[row_num][col_num] = '★'
        
    else:
        board[row_num][col_num] = '☆'

    return True

def switch_players(p1_p2):
    if p1_p2:
        return False
    else:
        return True
    
def handle_input(board, cmd, p1_p2, column_tally):
    valid_options = ['1','2','3','4','5','6','7']
    if cmd not in valid_options:
        return print('Your input was invalid')
    
    if valid_move(cmd, column_tally):
        if place_piece(board, cmd, p1_p2, column_tally):
            return True
    else:
        return False
    
def start_session(board):
    print_board(board)
    session = True
    winner = False
    p1_p2 = True
    column_tally = {}

    while session:
        cmd = input('Select a column (1-7): ')
        if handle_input(board, cmd, p1_p2, column_tally):
            print_board(board)
            winner = check_winner(board, cmd, p1_p2, column_tally)
            if winner:
                print('We Have a Winner')
                session = False
            p1_p2 = switch_players(p1_p2)
    print('game over')
 
def start_game():
    board = create_board()
    start_session(board)

start_game()
# print(check_row(['•','•', '★', '★', '★', '★', '•' ], True))
