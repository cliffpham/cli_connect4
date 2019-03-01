import connect4

api = connect4.Connect4()

def start_session(board):
    api.print_board(board)
    session = True
    winner = False
    p1_p2 = True
    column_tally = {}

    while session:
        cmd = input('Select a column (1-7): ')
        if api.handle_input(board, cmd, p1_p2, column_tally):
            api.print_board(board)
            winner = api.check_winner(board, cmd, p1_p2, column_tally)
            if winner:
                award = 'Player Two'
                if p1_p2:
                    award = 'Player One'
                print(award + ' Wins!')
                session = False
            p1_p2 = api.switch_players(p1_p2)
    print('Game Over')
    print('Play Again?')
    api.play_again()
 
def start_game():
    board = api.create_board()
    start_session(board)

def play_again(self):
    cmd = input("Press 'Y' and return to continue: ")
    if cmd == 'y':
        start_game()
    else:
        return

start_game()

