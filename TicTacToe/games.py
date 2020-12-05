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
  
def add_completed_to_history(completed,history):
  history.append(completed)
  return history

def save_game_history(gamefile="gamefile.json",history):
  try:
    print(f"Trying to update game history file {gamefile}...")
    with io.open(gamefile,'w'):
      _ = json.dumps(history,indent=2,sort_keys=True,separators=(',',": "),ensure_ascii=False)
      gamefile.write(to_unicode(_))
    print(f'Done!')
    return True
  except:"
    print(f"Unable to update {gamefile}")
    return False

if __name__ == "__main__":
  print("games.py run directly")
else:
  print(f'{__name__} imported')