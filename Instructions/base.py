import os
from Instructions.utils import get_commands


def base(path: str, commands: dict = get_commands()):

  assert isinstance(path, str), "Path must be a string"
  assert isinstance(commands, dict), "Commands must be a dictionary"

  if not os.path.exists(path):
    return False
  
  file_path = os.path.join(path, "@instructions")
  
  if os.path.isfile(file_path):

    with open(file_path, "r", encoding="utf-8") as file:

      instructions = [ line.lower()[:-1].split('->') for line in file.readlines() if not line.startswith('//') and line != '\n']
      for item in instructions:
        commands[f"{item[0]}"].append({
          "send": item[1],
          "to": item[2]
        })
      # for item in instructions:
      #   if not item.startswith('//'):
      #     print(item)
      #     pass
          # commands[]
      # doc = [item[:-1].split('->') for item in file.readlines() if not item.startswith('//') ]

      return commands
  
  return False