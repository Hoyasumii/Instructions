import sys, os

if __name__=="__main__":
  from path_resolve import path_resolve
  sys.path.append(os.getcwd())
  sys.path.append(path_resolve())

from Instructions.utils import list_args, path_resolve
from Instructions.models import ArgsList

INSTRUCTIONS_PATH = path_resolve()
COMMANDS_PATH = None
DESIRED_LAST_INDEX = -2
COMMANDS_PATH = os.path.join(INSTRUCTIONS_PATH, "commands") if __name__=="__main__" else f"{INSTRUCTIONS_PATH}\\commands"

def get_commands() -> dict:
  commands_files = os.listdir(COMMANDS_PATH)
  commands_files = [ file[:-3] for file in commands_files if os.path.isfile(f"{COMMANDS_PATH}\\{file}") and file != "__init__.py"]
  return { command: ArgsList(**list_args(command)) for command in commands_files }

if __name__=="__main__":
  print({key: value._pattern for key, value in get_commands().items()})
