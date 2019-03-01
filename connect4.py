class Connect4:
    def __init__(self):
        pass

    def create_board(self):
        board = []
        for _ in range(6):
            board.append(['•' for _ in range(7)])

        return board

    def print_board(self, board):
        for row in board:
            for spot in row:
                print(spot, end = " ")
            print()

    def check_rdiag(self,board, p1_p2, row, col):
        row_copy = row
        top_right = col
        check_for = '☆'
        cur_count = 0
        max_count = 0
        # row_copy = row

        if p1_p2:
            check_for = '★'

        while top_right < len(board):
            row_copy -= 1
            top_right += 1

        while row_copy < len(board):
            if board[row_copy][top_right] == check_for:
                # cur_count += 1
                r = row_copy 
                j = top_right 
                while r < len(board):
                    if board[r][j] == check_for:
                        cur_count += 1
                        max_count = max(cur_count, max_count)
                        if max_count == 4:
                            break
                        r += 1
                        j -= 1
                    else:
                        break
            cur_count = 0
            top_right -= 1
            row_copy += 1
        
        if max_count == 4:
            return True

        return False

    def check_ldiag(self, board, p1_p2, row, col):
        row_copy = row
        top_left = col
        check_for = '☆'
        cur_count = 0
        max_count = 0

        if p1_p2:
            check_for = '★'

        while top_left > 0:
            row_copy -= 1
            top_left -= 1

        while row_copy < len(board) - 1 and top_left < 7:
            # print(row_copy, top_left)
            if board[row_copy][top_left] == check_for:
                # cur_count += 1
                r = row_copy 
                j = top_left 
                while r < len(board) and j < 7:
                    if board[r][j] == check_for:
                        cur_count += 1
                        max_count = max(cur_count, max_count)
                        if max_count == 4:
                            break
                        r += 1
                        j += 1
                    else:
                        break
            cur_count = 0
            top_left += 1
            row_copy += 1
        
        if max_count == 4:
            return True

        return False
    
    def valid_move(self, cmd, column_tally):
        if cmd not in column_tally or column_tally[cmd] < 6:
            return True

        print('That column is filled up!')
        return False

    def find_row(self, n):
        ref = {0:5, 1:4, 2:3, 3:2, 4:1, 5:0}

        return ref[n]

    def check_col(self, board,p1_p2,col):
        check_for = '☆'
        max_count = 0
        cur_count = 0
        
        if p1_p2:
            check_for = '★'

        for i in range(len(board)-1, -1, -1):
            if board[i][col] == check_for:
                j = i
                while j < len(board):
                    if board[j][col] == check_for:
                        cur_count += 1
                        max_count = max(cur_count, max_count)
                        j+=1
                    else:
                        break
            cur_count = 0

        if max_count == 4:
            return True
        
        return False

    def check_row(self,board,p1_p2,row):
        check_for = '☆'
        max_count = 0
        cur_count = 0
        cur_row = board[row]
        
        # print('checking row')
        # print(cur_row)

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
        
        # print(max_count)
        if max_count == 4:
            return True
        else:
            return False

    def check_winner(self, board, cmd, p1_p2, column_tally):
        col = int(cmd)-1
        row = column_tally[cmd] - 1
        row = self.find_row(row)
    
        if self.check_row(board, p1_p2, row) or self.check_col(board, p1_p2, col) or self.check_ldiag(board, p1_p2, row, col) or self.check_rdiag(board, p1_p2, row, col):
            return True
        return False

    def place_piece(self, board, cmd, p1_p2, column_tally):
        col_num = int(cmd) - 1
        row_num = None

        if cmd in column_tally:
            row_num = column_tally[cmd]
            column_tally[cmd] += 1 
        else:
            row_num = 0
            column_tally[cmd] = 1

        row_num = self.find_row(row_num)

        if p1_p2:
            board[row_num][col_num] = '★'
            
        else:
            board[row_num][col_num] = '☆'

        return True

    def switch_players(self, p1_p2):
        if p1_p2:
            return False
        else:
            return True
        
    def handle_input(self, board, cmd, p1_p2, column_tally):
        valid_options = ['1','2','3','4','5','6','7']
        if cmd not in valid_options:
            return print('Your input was invalid')
        
        if self.valid_move(cmd, column_tally):
            if self.place_piece(board, cmd, p1_p2, column_tally):
                return True
        else:
            return False

    def play_again(self):
        cmd = input("Press 'Y' to continue: ")
        if cmd == 'y':
            self.start_game()
        else:
            return