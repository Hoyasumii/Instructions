import os, sys

def get_commands_from_path(path: str = __file__, commands_folder: str = "commands", dir_name: bool = False):

	assert isinstance(path, str), "Path must be a string"
	assert isinstance(commands_folder, str), "Commands folder must be a string"

	CORRECT_PATH = path if dir_name else os.path.dirname(path)

	sys.path.append(CORRECT_PATH)
	import utils.list_args as list_args
	import models.ArgsList as ArgsList

	COMMANDS_PATH = os.path.join((path if dir_name else os.path.dirname(path)), commands_folder)

	commands_files = [ command[:-3] for command in os.listdir(COMMANDS_PATH) if not command.startswith("_") and command.endswith(".py") ]

	return { command: ArgsList(**list_args(command, COMMANDS_PATH)) for command in commands_files }