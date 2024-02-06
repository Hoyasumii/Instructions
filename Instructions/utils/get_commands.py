import sys, os

INSTRUCTIONS_PATH = "\\".join(sys.path[0].split("\\")[:(-1 if __name__=="__main__" else None)])
COMMANDS_PATH = f"{INSTRUCTIONS_PATH}\\{"Instructions\\" if __name__!="__main__" else ""}commands"

def get_commands() -> dict:
  commands_files = os.listdir(COMMANDS_PATH)
  commands_files = [ file[:-3] for file in commands_files if os.path.isfile(f"{COMMANDS_PATH}\\{file}") and file != "__init__.py"]
  return { command: [] for command in commands_files }

if __name__=="__main__":
  print(get_commands())
  """
  
  insert: [
  {
  send: aaaa
  to: jknajkndsa
  }
  ]
  
  """