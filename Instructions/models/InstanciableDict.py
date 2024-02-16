class InstanciableDict:
	def __init__(self, **kwargs):
		for key, value in kwargs.items():
			setattr(self, key, value)
	
	def __dir__(self):
		return [attr for attr in dir(self) if not attr.startswith("__")]

	def __repr__(self):
		return f"[ {", ".join([f"'{attr}'" for attr in dir(self) if not attr.startswith("__")])} ]"

if __name__=='__main__':
  my_dict = { "name": "Alberto", "age": 20 }
  id = InstanciableDict(**my_dict)
  print(id.name)