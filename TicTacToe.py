#make board
#display game board
#take in players move and substitute

#global variables
player = "x"
game_continuation = True


board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

#the main game
#has all the functions in the right open
#works in a while loop until game_continuation is False
def tictactoe():
  while game_continuation == True:
    display_board()
    take_players_move()
    fluctuate_player()
    check_game_progress()


def display_board():
  print (board[0]+ " | " + board[1] + " | " + board[2])
  print (board[3] + " | " + board[4] + " | " + board[5])
  print (board[6] + " | " + board[7] + " | " + board[8])

def take_players_move():
  # Get position from player
  print(player + "'s turn.")
  position = input("Choose a position from 1-9: ")

  # Whatever the user inputs, make sure it is a valid input, and the spot is open
  valid = False
  while not valid:

    # Make sure the input is valid
    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      position = input("Choose a position from 1-9: ")
 
    # Get correct index in our board list
    position = int(position) - 1

    # Then also make sure the spot is available on the board
    if board[position] == "-":
      valid = True
    else:
      print("Please enter into an empty space. Try again.")

  # Put the game piece on the board
  board[position] = player

def fluctuate_player():
  global player
  if player == "x":
    player = "o"
  else:
    player = "x"  

def check_game_progress():
  #Global row_win
  #Global Column_win
  #Global Diagonal_win
  row_win()
  column_win()
  diagonal_win()
  if game_continuation == True:
    tictactoe()
  else:
    display_board()
    fluctuate_player()
    print (player + " won!")  



#Checking if the game has ended


#checking row wise
def row_win():
  global game_continuation
  if (board[0] == board[1] == board[2]) and (board[0] != "-"):
    game_continuation = False
  elif (board[3] == board[4] == board[5]) and (board[3] != "-"):
    game_continuation = False
  elif (board[6] == board[7] == board[8]) and (board[6] != "-"):
    game_continuation = False
  elif "-" not in board:
    game_continuation = False
    print ("The game is a draw")
  return

#checking column wise
def column_win():
  global game_continuation
  if (board[0] == board[3] == board[6]) and (board[0] != "-"):
    game_continuation = False
  elif (board[1] == board[4] == board[7]) and (board[1] != "-"):
    game_continuation = False
  elif (board[2] == board[5] == board[8]) and (board[2] != "-"):
    game_continuation = False
  elif "-" not in board:
    game_continuation = False
    print ("The game is a draw")  
  return   

#checking diagonal wise
def diagonal_win():
  global game_continuation
  if (board[0] == board[4] == board[8]) and (board[0] != "-"):
    game_continuation = False
  elif (board[2] == board[4] == board[6]) and (board[2] != "-"):
    game_continuation = False
  elif "-" not in board:
    game_continuation = False
    print ("The game is a draw")   
  return    


tictactoe()


