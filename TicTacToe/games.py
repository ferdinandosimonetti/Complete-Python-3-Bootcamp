import json
import io
import random

try:
  to_unicode = unicode
except NameError:
  to_unicode = str

def build_completed_game(moves,outcome):
  return {'moves': moves, 'outcome': outcome}

def load_game_history(gamefile="gamefile.json"):
  try:
    print(f"Loading game history file {gamefile}...")
    with io.open(gamefile) as datafile:
      # will be a list
      return json.load(datafile)
  except FileNotFoundError:
    print(f"Creating new game history...")
    with io.open(gamefile,'w') as datafile:
      return []
  except PermissionError:
    print(f"No read permission on {gamefile}")
  
def add_completed_to_history(completed,history):
  if completed not in history:
    history.append(completed)
  return history

def save_game_history(history,gamefile="gamefile.json"):
  try:
    print(f"Trying to update game history file {gamefile}...")
    with io.open(gamefile,'w') as datafile:
      _ = json.dumps(history,indent=2,sort_keys=True,separators=(',',": "),ensure_ascii=False)
      datafile.write(to_unicode(_))
    print(f'Done!')
    return True
  except Exception as e:
    print(f"Unable to update {gamefile}")
    print(str(e))
    return False

def extract_from_history(history,moves,desired="O"):
  return [_ for _ in history if _['moves'].startswith(moves) and _['outcome'] == desired]

def next_moves(history,moves):
  # how many moves so far? Opponent has already played, now our turn
  moveslength = len(moves)
  # extract our moves in the past that led to victory
  playedmoves = [_[moveslength+1] for _ in history['moves']]
  # unique moves
  return set(playedmoves)

def random_move(moves):
  # using intermediate variables for clarity's sake
  fulltable = [str(i) for i in range(0,9)]
  moveslist = [ i for i in moves ]
  possible = [ i for i in fulltable if i not in set(moveslist)]
  return random.choice(possible)

def best_move(history,moves,desired='O'):
  # look for matches won from here
  wingames = extract_from_history(history,moves,desired)
  # there are none, going random
  if len(wingames) == 0:
    return random_move(moves)
  # there are one or more
  else:
    wins = 0
    bestmove = ''
    # for each distinct move played in the past
    for _ in next_moves(history,moves):
      # determine how many times the current move led to victory
      numwins = len(extract_from_history(history,moves+_,desired=desired))
      # if it's higher than the previous, set new 'wins' and best 'move' so far
      if numwins > wins:
        wins = numwins
        bestmove = _
    return bestmove


if __name__ == "__main__":
  print('games.py run directly')
else:
  print(f'{__name__} imported')