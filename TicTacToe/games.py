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

def extract_from_history(history,moves,desired="X"):
  return [_ for _ in history if _['moves'].startswith(moves) and _['outcome'] == desired]

def random_move(moves):
  # using intermediate variables for clarity's sake
  fulltable = [str(i) for i in range(0,9)]
  moveslist = [ i for i in moves ]
  possible = [ i for i in fulltable if i not in set(moveslist)]
  return random.choice(possible)

def dont_loose(history,moves):
  # look for matches lost from here
  lostgames = extract_from_history(history,moves)
  losthistories = [ _['moves'] for _ in lostgames ]
  #losingmoves = [ _[len(moves)] for _ in losthistories ]
  print(losthistories)
  #print(losingmoves)
  #dontplaythesemoves = moves + ''.join(set(losingmoves))
  #print(dontplaythesemoves)
  _ = input("press any key")
  # play randomly... 
  return random_move(moves)

if __name__ == "__main__":
  print('games.py run directly')
else:
  print(f'{__name__} imported')