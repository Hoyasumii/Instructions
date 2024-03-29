import os, importlib.util

if __name__=="__main__":
	from utils import get_commands, get_commands_from_path, list_args, load_command, get_instructions
else:
	from Instructions.utils import get_commands, get_commands_from_path, list_args, load_command, get_instructions

class Instructions:

	_EXTENSIBLE_COMMANDS = None
	
	def __init__(self, path: str = os.getcwd(), ignore_if_not_found: bool = False):
		assert isinstance(path, str), "Path must be a string"

		if not os.path.exists(path):
			raise FileNotFoundError("Path not found")
		
		self._EXTENSIBLE_COMMANDS = True if os.path.exists(os.path.join(path, "@commands")) else False
				
		self.commands_path = os.path.join(path, "Instructions\\commands")

		if __name__!="__main__":
			self.commands_path = importlib.util.find_spec("Instructions.commands").origin
			self.commands_path = self.commands_path[:self.commands_path.rfind("\\")]

		self.personal_commands_path = os.path.join(path, "@commands")

		self.file_path = os.path.join(path, "@instructions")

		if not os.path.isfile(self.file_path):
			raise FileNotFoundError("@instructions file not found")

		self.commands = get_commands()

		if self._EXTENSIBLE_COMMANDS:
			personal_commands = get_commands_from_path(__file__, self.personal_commands_path)

		merged_commands = set(self.commands) & set(personal_commands)

		if merged_commands:
			raise ValueError(f"You cannot create a command with the same name as an existing command{"s" if len(merged_commands) > 1 else ""}: {merged_commands}")

		self.commands.update(personal_commands)

		with open(self.file_path, "r", encoding="utf-8") as file:

			instructions = get_instructions(file)

			for item in instructions:
				try:
					command_args = list_args(item[0], self.commands_path)
					args = { param: arg for param, arg in list(zip(command_args.keys(), item[1:])) }
					self.commands[item[0]].append(**args)

				except FileNotFoundError:
					try:
						command_args = list_args(item[0], self.personal_commands_path)
						args = { param: arg for param, arg in list(zip(command_args.keys(), item[1:])) }
						self.commands[item[0]].append(**args)

					except FileNotFoundError:

						if ignore_if_not_found:
							continue
						
						raise FileNotFoundError(f"Command {item[0]} not found")

	def run(self):
		for command, args in self.commands.items():
			if args.args_len == 0 and not args[0] is None:
				try:
					for _ in range(len(args)):
						getattr(load_command(command, self.commands_path), command)()
				except FileNotFoundError:
					for _ in range(len(args)):
						getattr(load_command(command, self.personal_commands_path), command)()
				continue

			for arg in args:
				if not arg:		
					break
				try:
					getattr(load_command(command, self.commands_path), command)(**arg)
				except FileNotFoundError:
					getattr(load_command(command, self.personal_commands_path), command)(**arg)

	def __call__(self):
		return self.run()
  
if __name__=="__main__":
  commands = Instructions()
  commands.run()