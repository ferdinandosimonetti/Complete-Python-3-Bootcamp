from operator import itemgetter
from os import system, name
from time import sleep

# I want to use a simple monodimensional list for the gametable
# I have to find a way to select discontinuous elements of a list
col1 = itemgetter(0,3,6)
col2 = itemgetter(1,4,7)
col3 = itemgetter(2,5,8)
dia1 = itemgetter(0,4,8)
dia2 = itemgetter(2,4,6)

def initialize():
  '''
  The list representing the game table is filled with "-" placeholders
  '''
  global gametable
  gametable = []
  for _ in range(0,9):
    gametable.append('-')

def clearscreen():
  '''
  How to discover if you're running inside a Jupyter notebook???
  '''
  if name == 'nt':
    _ = system('cls')
  else:
    _ = system('clear')
    
def redraw():
  '''
  Definitely cut some corners here, the table is not at all fancy.
  I'm drawing the game table by subdividing the representing list in three rows.
  '''
  global gametable
  sleep(1)
  clearscreen()
  print (''.join(gametable[:3]))
  print (''.join(gametable[3:6]))
  print (''.join(gametable[6:9]))


def win(player):
  '''
  Ugly way to find out if someone has won
  There should be a better way
  '''
  global gametable
  haswon = False
  # first row
  if set(gametable[0:3]) == set(player):
    haswon = True
  # second row
  if set(gametable[3:6]) == set(player):
    haswon = True
  # third row
  if set(gametable[6:9]) == set(player):
    haswon = True
  # first column, via itemgetter...
  if set(col1(gametable)) == set(player):
    haswon = True
  # second column, itemgetter again
  if set(col2(gametable)) == set(player):
    haswon = True
  # third column, itemgetter to the rescue
  if set(col3(gametable)) == set(player):
    haswon = True
  # first diagonal...
  if set(dia1(gametable)) == set(player):
    haswon = True
  # and the second diagonal
  if set(dia2(gametable)) == set(player):
    haswon = True
  if haswon:
    print(f'{player} has won!')
  return haswon


def fulltable():
  '''
  If there are no more '-'s inside the list, the game has ended!
  '''
  global gametable
  if '-' not in gametable:
    print("The game has ended in a draw! No more playable moves.")
    return True
  return False 

# Find out if the player's move is legal
def playablemove(move):
  '''
  You can only play where the table is still empty
  '''
  global gametable
  # if the input is between '0' and '8'
  if move in (str(i) for i in range(0,9)):
    # if the chosen position is still empty
    if gametable[int(move)] == "-":
      return True
  return False 

# Ask the player to select a move
def playermove():
  global move
  plmove = input("Make your move (0..8): ")
  if playablemove(plmove):
    move = plmove
    return True
  print("Illegal move!")
  return False

# Initialize an empty list
gametable = []
# Initialize an obviously illegal move
move = "#"

# Start game, the table is empty
initialize()
redraw()

print("X plays first, then O")
player = 'X'

# while loop continues until X wins, O wins or there are no more playable moves
while not win('X') and not win('O') and not fulltable():
  print(f"It's {player} turn!")
  # internal while loop continues until the player provides a 'legal' move
  while not playermove():
    pass
  # list is updated
  gametable[int(move)] = player
  # and game table is redrawn
  redraw()
  # players should alternate
  if player == 'X':
    player = 'O'
  else:
    player = 'X'

print('End game')