import os, importlib.util

def load_command(command_name: str, path: str = os.path.dirname(__file__)):

	assert isinstance(command_name, str), "The command must be a string"
	assert isinstance(path, str), "Path must be a string"

	spec = importlib.util.spec_from_file_location(command_name, f"{path}\\{command_name}.py")
	module = importlib.util.module_from_spec(spec)
	spec.loader.exec_module(module)
	
	return module