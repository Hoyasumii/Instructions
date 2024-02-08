import os
from Instructions.utils import get_commands, list_args

def base(path: str, commands: dict = get_commands()):

  assert isinstance(path, str), "Path must be a string"
  assert isinstance(commands, dict), "Commands must be a dictionary"

  if not os.path.exists(path):
    return False
  
  file_path = os.path.join(path, "@instructions")
  
  if os.path.isfile(file_path):

    with open(file_path, "r", encoding="utf-8") as file:

      instructions = [ line[:(-1 if line.endswith("\n") else None)].split('->') for line in file.readlines() if not line.startswith('//') and line != '\n']

      for arg in instructions:
        arg[0] = arg[0].lower()

      for item in instructions:
        command_args = list_args(item[0])
        args = { param: arg for param, arg in list(zip(command_args.keys(), item[1:])) }
        commands[item[0]].append(**args)

      return commands
  
  return False