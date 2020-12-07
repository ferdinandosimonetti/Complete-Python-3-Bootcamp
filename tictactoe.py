#from TicTacToe import initialize,clearscreen,redraw,fulltable,playablemove,playermove,win
from TicTacToe import *
# empty table
gametable = []
# obviously illegal move
move      = "#"

moves = ""
outcome = ""

if __name__ == "__main__":
  # Start game, the table is empty
  gametable = initialize(gametable)
  redraw(gametable)
  # load previous game history file
  gamehistory = load_game_history()
  # ask if p1 vs p2 or p1 vs computer
  playerchoice = '#'
  computerplayso = False
  while playerchoice not in ('y','n'):
    playerchoice = input("Should computer play as O? [Yy/Nn]").lower()
  if playerchoice == 'y':
    computerplayso = True

  print("X plays first, then O")
  player = 'X'

  # while loop continues until X wins, O wins or there are no more playable moves
  while not win('X',gametable) and not win('O',gametable) and not fulltable(gametable):
    print(f"It's {player} turn!")
    # internal while loop continues until the player provides a 'legal' move
    while True:
      # it's O turn and O is computer?
      if player == 'O' and computerplayso:
        status, move = True, dont_loose(gamehistory,moves)
      else:
        status, move = playermove(move,gametable)
      if status:
        break
    # list is updated
    gametable[int(move)] = player
    # match history is updated
    moves += move
    # and game table is redrawn
    redraw(gametable)
    # players should alternate
    if player == 'X':
      player = 'O'
    else:
      player = 'X'
    
  # update the outcome
  if win('X',gametable,announce=False):
    outcome = 'X'
  elif win('O',gametable,announce=False):
    outcome = 'O'
  # update gamehistory
  gamehistory = add_completed_to_history(build_completed_game(moves,outcome),gamehistory)
  # and save it to file
  if save_game_history(gamehistory):
    print("GAME HISTORY SAVED OK!")
  else:
    print("GAME HISTORY SAVE KO!!!")
  print('End game')