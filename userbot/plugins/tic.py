import random
from time import sleep

class Board:
    def __init__(self):
        self.board = [[' ' for cols in range(3)] for rows in range(3)]
        
        self.X = 'x'
        self.O = 'o'
        self.Star = '*'

    def __getitem__(self, index):
        return self.board[index]
        

def get_coords():
    return [
        # VERTICAL LINES
        [(1, 1), (1, 2), (1, 3)],
        [(2, 1), (2, 2), (2, 3)],
        [(3, 1), (3, 2), (3, 3)],
        # HORIZONTAL LINES
        [(1, 1), (2, 1), (3, 1)],
        [(1, 2), (2, 2), (3, 2)],
        [(1, 3), (2, 3), (3, 3)],
        # DIAGONALS
        [(1, 1), (2, 2), (3, 3)],
        [(1, 3), (2, 2), (3, 1)],
    ].copy()


def get_right_index(indices, coords, board):
    for c in coords:
        if c not in indices:
            x, y = (i-1 for i in c)
            if board[x][y] == ' ':
                return True, x, y
            else: return False, -1, -1


def user_turn(board):
    print("Your turn!")
    while True:
        try:
            x, y, *_ = input("Enter cell <x, y>: ").split(',')
            x, y = int(x)-1, int(y)-1
        except:
            print("Invalid Input")
            print()
            continue
        if ((x > 2 or x < 0) or 
           (y > 2 or y < 0)):
            print("The cell doesn't exist")
            print()
            continue
        elif board[x][y] == ' ':
            board[x][y] = board.X
            break
        else:
            print("Choose a different cell")
            print()
            continue


def computer_turn(board):
    print("Computer's turn!")
    sleep(1.5)
        
    winning_coords = get_coords()
    user_lines = []
    user_coords = []
    comp_lines = []
    comp_coords = []

    for coords in winning_coords:
        user_line_indices = set()
        comp_line_indices = set()
        for index, (x, y) in enumerate(coords):
            if board[x-1][y-1] == board.X:
                user_line_indices.add((x, y))
            elif board[x-1][y-1] == board.O:
                comp_line_indices.add((x, y))
            
        if len(comp_line_indices) == 2:
            comp_lines.append(comp_line_indices)
            comp_coords.append(coords)
        if len(user_line_indices) == 2:
            user_lines.append(user_line_indices)
            user_coords.append(coords)
            
    for comp_line_indices, coords in zip(comp_lines, comp_coords):
        success, x, y = get_right_index(comp_line_indices, coords, board)
        if success: break
    else:
        for user_line_indices, coords in zip(user_lines, user_coords):
            success, x, y = get_right_index(user_line_indices, coords, board)
            if success: break
        else:
            if board[1][1] == ' ':
                x, y = 1, 1
            else:
                while True:
                    x, y = random.choice([0, 2]), random.choice([0, 2]) 
                    if board[x][y] == ' ': break
    
    board[x][y] = board.O


def check_win(board):
    winning_coords = get_coords()
   
    for coords in winning_coords:
        user_line_count = 0
        comp_line_count = 0
        for (x, y) in coords:
            if board[x-1][y-1] == board.X:
                user_line_count += 1
            elif board[x-1][y-1] == board.O:
                comp_line_count += 1
        
        if (user_line_count == 3 or
        	   comp_line_count == 3):
            for x, y in coords:
                board[x-1][y-1] = board.Star
            generate_board(board)

        if user_line_count == 3:
            print("You won!")
            return True
        elif comp_line_count == 3:
            print("You lost!")
            return True
        elif is_full(board):
            print("It's a tie!")
            return True
    return False


def is_full(board):
    empty_count = 0
    for row in board:
        for element in row:
            if element == ' ':
                empty_count += 1
    
    return not empty_count


def generate_board(*args, dummy=False):
    if args and isinstance(args[0], Board):
        board_list = args[0].board

    if dummy:
        board_str_list = [' | '.join([f'{x},{y}' for y in range(1, 4)]) for x in range(1, 4)]
    else:
        board_str_list = [' | '.join([board[x][y] for y in range(3)]) for x in range(3)]
    
    padding_line = '-'*len(board_str_list[0])
    board_string = f'\n{padding_line}\n'.join(board_str_list)
    
    print()
    print(board_string)
    print()

if __name__ == '__main__':
    print("Welcome to The Pythonic TicTacToe!")
    print("The board's co-ordinates are as follows:")
    generate_board(dummy=True)
    
    while True:
        print('-'*20)
        board = Board()
        
        while True:
            generate_board(board)
            user_turn(board)
            if check_win(board): break
            generate_board(board)
            computer_turn(board)
            if check_win(board): break
        
        user_input = input("Enter R to Restart. ").lower()
        if user_input != 'r':
            break
    