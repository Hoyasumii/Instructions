import inspect


if __name__=="__main__":
	from InstanciableDict import InstanciableDict
else:
	from .InstanciableDict import InstanciableDict

class ArgsList:
	def __init__(self, **kwargs):
		self._pattern = { **kwargs }
		self._data = []

	def append(self, **kwargs):
		self._validate(**kwargs)
		casted_kwargs = self._casting(**kwargs)
		self._data.append({ **casted_kwargs })

	def _validate(self, **kwargs):
		
		# The number of keys must be equal to the number of args
		number_of_keys = len(self._pattern.keys())
		number_of_args = len(kwargs.keys())
		assert number_of_keys == number_of_args, f"The number of keys must be equal to the number of args. Expected {number_of_keys} but got {number_of_args}"

		# The keys must be equal to the pattern
		for key in kwargs.keys():
			assert key in self._pattern.keys(), f"Key {key} is not in the pattern"
				
	def _casting(self, **kwargs) -> dict:
		try:
			for key, value in kwargs.items():
				if self._pattern[key] == inspect._empty:
					continue
				kwargs[key] = self._pattern[key](value)
		except ValueError:
			raise ValueError(f"Value {value} is not castable to {self._pattern[key]}")
		return kwargs

	def __getitem__(self, index):
		assert isinstance(index, int), "The index must be an integer"

		try:
			return self._data[index]
		
		except IndexError:
			return None

	def __len__(self) -> int:
		return self._data.__len__()

	def __repr__(self) -> str:
		return self._data.__repr__()

if __name__=="__main__":
  args = ArgsList(a=int, b=int, c=int)
  args.append(a=1, b=2, c=3)
  args.append(a=4, b=5, c=6)
  print(args[0].a)