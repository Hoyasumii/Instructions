import sys, os

INSTRUCTIONS_PATH = None
COMMANDS_PATH = None
DESIRED_LAST_INDEX = -2

print(sys.path[0])

INSTRUCTIONS_PATH = "\\".join(os.path.join(sys.path[0], "Instructions").split("\\")[:DESIRED_LAST_INDEX])
COMMANDS_PATH = os.path.join(INSTRUCTIONS_PATH, "commands") if __name__=="__main__" else f"{INSTRUCTIONS_PATH}\\commands"

def get_commands() -> dict:
  # print(COMMANDS_PATH)
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