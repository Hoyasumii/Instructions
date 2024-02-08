import inspect, importlib, os, pkgutil, sys

if __name__=="__main__":
  sys.path.append(os.getcwd())
  sys.path.append(os.path.join(sys.path[0], "Instructions"))

def list_args(commandName: str) -> dict:

  assert isinstance(commandName, str), "The command must be a string"

  # The module contains ONE command
  commandModule = importlib.import_module(f"Instructions.commands.{commandName}") 

  if getattr(commandModule, commandName):
    return { key: None for key in inspect.signature(getattr(commandModule, commandName)).parameters.keys() }
  
  return {}

if __name__=="__main__":
  print(list_args("insert"))