def display_board(board):
  blankBoard="""
     ___________
    | 7 | 8 | 9 |
     ___________
    | 4 | 5 | 6 |
     ___________
    | 1 | 2 | 3 |
     ___________
"""
  for i in range(1,10):
    if (board[i] == 'O' or board[i] == 'X'):
      blankBoard = blankBoard.replace(str(i), board[i])
    else:
      blankBoard = blankBoard.replace(str(i), ' ')
  print(blankBoard)
  
def player_input():
  player1 = input("Please type X or O to pick your symbol: ")
  while True:
    if player1.upper() == 'X':
      player2 = 'O'
      print("You have chosen " + player1 + ". Player 2 is " + player2)
      return player1.upper(), player2
    elif player1.upper() == 'O':
      player2 = 'X'
      print("You have chosen " + player1 + ". Player 2 is " + player2)
      return player1.upper(), player2
    else:
      player1 = input("Not a valid input. Please type X or O to pick your symbol: ")
      
def place_marker(board, marker, position):
  board[position] = marker
  return board

def space_check(board, position):
  return board[position] == '#'

def player_choice(board):
  choice = input("Please select an empty space between 1 and 9: ")
  while not space_check(board, int(choice)):
    choice = input("Sorry, that wasn't a valid input. Make sure your space is free and between 1 and 9: ")
  return choice

def full_board_check(board):
  return len([x for x in board if x =='#']) == 1

def win_check(board, mark):
    if board[1] == board[2] == board[3] == mark:
        return True
    if board[4] == board[5] == board[6] == mark:
        return True
    if board[7] == board[8] == board[9] == mark:
        return True
    if board[1] == board[4] == board[7] == mark:
        return True
    if board[2] == board[5] == board[8] == mark:
        return True
    if board[3] == board[6] == board[9] == mark:
        return True
    if board[1] == board[5] == board[9] == mark:
        return True
    if board[3] == board[5] == board[7] == mark:
        return True
    return False
  
def replay():
  playAgain = input("Do you want to play again? (Y = Yes, other input = No): ")
  if playAgain.upper() == 'Y':
    return True
  else:
    return False   
  
if __name__ == "__main__":
  print("Starting Tic-Tac-Toe")
  # Keep track of player
  playerTurn = 1
  players=player_input()
  # Make board (# is empty)
  board = ['#'] * 10
  while True:
    game_on=full_board_check(board)
    while not game_on:
      # Player picks location
      print("It's " + players[not playerTurn % 2] + "'s turn!")
      position = player_choice(board)
      # Player 2's turn if playerTurn is even, vice versa
      if playerTurn % 2 == 0:
        marker = players[1]
      else:
        marker = players[0]
      # Place marker
      place_marker(board, marker, int(position))
      # View board
      display_board(board)
      # Advance turn
      playerTurn += 1
      # Check for a win
      if win_check(board, marker):
        print(players[playerTurn % 2] + " won!")
        break
      game_on = full_board_check(board)
    if not replay():
      break
    else:
      playerTurn = 1
      players=player_input()
      # Make board (# is empty)
      board = ['#'] * 10
