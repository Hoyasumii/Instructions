import importlib.util, importlib

if __name__=="__main__":
    from get_commands_from_path import get_commands_from_path
else:
    from Instructions.utils import get_commands_from_path

def get_commands():
    instructions_lib_path = importlib.util.find_spec("Instructions").origin
    return get_commands_from_path(instructions_lib_path)

if __name__=="__main__":
    print(get_commands())