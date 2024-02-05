import importlib, os, sys, inspect

def run(data: dict):
  
  assert isinstance(data, dict), "Data must be a dictionary"

  for key, value in data.items():
    commands = importlib.import_module(f'Instructions.commands')
    numberOfArgs = len(inspect.signature(getattr(commands, key)).parameters)
    getattr(commands, key)(*value[0:numberOfArgs])
