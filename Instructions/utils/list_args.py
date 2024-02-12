import inspect, importlib.util, os

def list_args(command_name: str, path: str = os.path.dirname(__file__)) -> dict:

	assert isinstance(command_name, str), "The command must be a string"
	assert isinstance(path, str), "Path must be a string"	

	spec = importlib.util.spec_from_file_location(command_name, f"{path}\\{command_name}.py")
	module = importlib.util.module_from_spec(spec)
	spec.loader.exec_module(module)

	return { key: None for key in inspect.signature(getattr(module, command_name)).parameters.keys() }

if __name__=="__main__":
	current_path = "\\".join(os.path.dirname(__file__).split("\\")[:-1])
	current_path += "\\commands"

	print(list_args("insert", current_path))