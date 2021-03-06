from operator import itemgetter
from os import system, name
from time import sleep

# I want to use a simple monodimensional list for the gametable
# I have to find a way to select discontinuous elements of a list
# this is a list of functions
checker = []
checker.append(itemgetter(0,3,6))
checker.append(itemgetter(1,4,7))
checker.append(itemgetter(2,5,8))
checker.append(itemgetter(0,4,8))
checker.append(itemgetter(2,4,6))
# no real need to use itemgetter because not discontinuous
# but I keep using it for consistency
checker.append(itemgetter(0,1,2))
checker.append(itemgetter(3,4,5))
checker.append(itemgetter(6,7,8))

def initialize(gametable):
  '''
  The list representing the game table is filled with "-" placeholders
  '''
  gametable = []
  for _ in range(0,9):
    gametable.append('-')
  return gametable

def clearscreen():
  '''
  How to discover if you're running inside a Jupyter notebook???
  '''
  if name == 'nt':
    _ = system('cls')
  else:
    _ = system('clear')
    
def redraw(gametable):
  '''
  Definitely cut some corners here, the table is not at all fancy.
  I'm drawing the game table by subdividing the representing list in three rows.
  '''
  sleep(1)
  clearscreen()
  print (''.join(gametable[:3]))
  print (''.join(gametable[3:6]))
  print (''.join(gametable[6:9]))


def win(player,gametable):
  '''
  It's better than eight "if"s
  But it's not very readable
  '''
  haswon = 0
  for _ in checker:
    haswon += (set(_(gametable)) == set(player))
  if haswon:
    print(f'{player} has won!')
  return bool(haswon)

def fulltable(gametable):
  '''
  If there are no more '-'s inside the list, the game has ended!
  '''
  if '-' not in gametable:
    print("The game has ended in a draw! No more playable moves.")
    return True
  return False 

# Find out if the player's move is legal
def playablemove(move,gametable):
  '''
  You can only play where the table is still empty
  '''
  # if the input is between '0' and '8'
  if move in (str(i) for i in range(0,9)):
    # if the chosen position is still empty
    if gametable[int(move)] == "-":
      return True
  return False 

# Ask the player to select a move
def playermove(gametable):
  global move
  plmove = input("Make your move (0..8): ")
  if playablemove(plmove,gametable):
    move = plmove
    return True
  print("Illegal move!")
  return False

# Initialize an empty list
gametable = []
# Initialize an obviously illegal move
move = "#"

# Start game, the table is empty
gametable = initialize(gametable)
redraw(gametable)

print("X plays first, then O")
player = 'X'

# while loop continues until X wins, O wins or there are no more playable moves
while not win('X',gametable) and not win('O',gametable) and not fulltable(gametable):
  print(f"It's {player} turn!")
  # internal while loop continues until the player provides a 'legal' move
  while not playermove(gametable):
    pass
  # list is updated
  gametable[int(move)] = player
  # and game table is redrawn
  redraw(gametable)
  # players should alternate
  if player == 'X':
    player = 'O'
  else:
    player = 'X'

print('End game')