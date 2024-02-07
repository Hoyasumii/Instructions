import inspect, importlib, os, pkgutil, sys

if __name__=="__main__":
  sys.path.append(os.getcwd())
  sys.path.append(os.path.join(sys.path[0], "Instructions"))

def list_args(command: callable):
  print(inspect.signature(command).parameters)
  # module = importlib.import_module("Instructions.commands.insert")
  # commands = pkgutil.iter_modules(["./Instructions/commands"])

  # for command in commands:
  #   module = importlib.import_module(f"Instructions.commands.{command.name}")
    
  #   if module:
  #     module = module.load_module()

  #     print(inspect.signature(module).parameters)

if __name__=="__main__":
  commands = pkgutil.iter_modules(["./Instructions/commands"])
  commands = [ importlib.import_module(f"Instructions.commands.{command.name}") for command in commands ]
  for command in commands:
    if command:
      print([command for command in dir(command) if not command.startswith("__")])
      print({ key: value.annotation for key, value in inspect.signature(getattr(command, "insert")).parameters.items()})
      # list_args(command.__loader__)
  # [ command.__loader__ for command in commands ]
  # [ inspect.signature(command).parameters for command in commands]
  # list_args(commands[0])