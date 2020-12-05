from TicTacToe import initialize,clearscreen,redraw,fulltable,playablemove,playermove,win
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

  print("X plays first, then O")
  player = 'X'

  # while loop continues until X wins, O wins or there are no more playable moves
  while not win('X',gametable) and not win('O',gametable) and not fulltable(gametable):
    print(f"It's {player} turn!")
    # internal while loop continues until the player provides a 'legal' move
    while True:
      status, move = playermove(move,gametable)
      if status:
        break
    # list is updated
    gametable[int(move)] = player
    # match history is updated
    
    # and game table is redrawn
    redraw(gametable)
    # players should alternate
    if player == 'X':
      player = 'O'
    else:
      player = 'X'
    
    print('End game')