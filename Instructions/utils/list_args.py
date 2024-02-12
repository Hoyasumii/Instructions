import inspect, os

if __name__=="__main__":
	from load_command import load_command
elif __name__=="utils.list_args":
	from utils.load_command import load_command
else:
	from Instructions.utils.load_command import load_command

def list_args(command_name: str, path: str = os.path.dirname(__file__)) -> dict:

	assert isinstance(command_name, str), "The command must be a string"
	assert isinstance(path, str), "Path must be a string"

	module = load_command(command_name, path)

	return { key: param.annotation for key, param in inspect.signature(getattr(module, command_name)).parameters.items() }

if __name__=="__main__":
	current_path = "\\".join(os.path.dirname(__file__).split("\\")[:-1])
	current_path += "\\commands"