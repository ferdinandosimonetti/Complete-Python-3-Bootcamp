import json
import io

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

if __name__ == "__main__":
  print("games.py run directly, tests should be run")
  # load previous history (not existent on first run)
  gamehistory = load_game_history("test.json")
  # the match has finished
  moves = "104753628"
  # with a draw
  outcome = ""
  # update game history in memory
  gamehistory = add_completed_to_history(build_completed_game(moves,outcome),gamehistory)
  # and saving it to file
  if save_game_history(gamehistory,gamefile="test.json"):
    print("OK!!!")
  else:
    print("SAVE KO!!!")
    exit()
  # load previous history (now should exist)
  gamehistory = load_game_history("test.json")
  # the match has finished
  moves = "4071286"
  # X wins|
  outcome = "X"
  # update game history in memory
  gamehistory = add_completed_to_history(build_completed_game(moves,outcome),gamehistory)
  # and saving it to file
  if save_game_history(gamehistory,gamefile="test.json"):
    print("OK!!!")
  else:
    print("SAVE KO!!!")
    exit()
else:
  print(f'{__name__} imported')