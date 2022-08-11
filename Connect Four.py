import numpy as np

PLAYER = 1
ROW_COUNT = 6
COLUMN_COUNT = 7

board_maker = lambda : np.zeros((ROW_COUNT,COLUMN_COUNT))
board = board_maker()






#checks if the top row of the selected column is empty, i.e if the column is full or not and returns a boolean value
def check_col_empty(board,col_number):
    return board[ROW_COUNT-1][col_number] == 0

#returns the next empty row in the selected column
def select_which_row(board,col_number):
    for _ in range(ROW_COUNT):
        if board[_][col_number] == 0:
            return _    

#drops the piece onto the finalized row and column
def piece_drop(game_board,row_number,col_number,player_input):
    game_board[row_number][col_number] = player_input
    return game_board


#swaps the player each turn for a two player game
def fluctuate_player():
    global PLAYER
    if PLAYER == 1:
        PLAYER = 2
    else:
        PLAYER = 1   
    return PLAYER 






#checks win by seeing similar elements across columns 
def check_vertical_win(board, piece):

	for c in range(COLUMN_COUNT-3):
		for r in range(ROW_COUNT):
			if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
				return True

#checks win by seeing similar elements across rows 
def check_horizontal_win(board, piece):
	for r in range(ROW_COUNT-3):
		for c in range(COLUMN_COUNT):
			if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
				return True

def check_positive_diagonal_win(board, piece):
	for c in range(COLUMN_COUNT-3):
		for r in range(ROW_COUNT-3):
			if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
				return True

def check_negative_diagonal_win(board, piece):
	for c in range(COLUMN_COUNT-3):
		for r in range(3, ROW_COUNT):
			if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
				return True


                





#this function calls all the other functions and is how you start the actual game
def play_game():
    global PLAYER
    global board
    while True:
            print(np.flip(board, 0),'\n')  
            if check_vertical_win(board,PLAYER) or check_horizontal_win(board,PLAYER) or check_negative_diagonal_win(board,PLAYER) or check_positive_diagonal_win(board,PLAYER): 
              print("CONGRATSSS YOU WON, PLAYER " + str(PLAYER))
              break

            #if PLAYER == 1:
            col = int(input("Player " + str(PLAYER) + ", please enter the column number (1-6)"))
            #else:
              #col = rd.randint(0,6)
            
            col -= 1

            if check_col_empty(board,col):
              row = select_which_row(board,col)
            piece_drop(board,row,col,PLAYER)
            
            fluctuate_player()




play_game()    
