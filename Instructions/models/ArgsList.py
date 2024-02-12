if __name__=="__main__":
	from InstanciableDict import InstanciableDict
else:
	from .InstanciableDict import InstanciableDict

class ArgsList:
	def __init__(self, **kwars):
		self._pattern = { **kwars }
		self._data = []

	def append(self, **kwars):
		self._validate(**kwars)
		self._data.append({ **kwars })

	def _validate(self, **kwars):
		
		# The number of keys must be equal to the number of args
		number_of_keys = len(self._pattern.keys())
		number_of_args = len(kwars.keys())
		assert number_of_keys == number_of_args, f"The number of keys must be equal to the number of args. Expected {number_of_keys} but got {number_of_args}"

		# The keys must be equal to the pattern
		for key in kwars.keys():
			assert key in self._pattern.keys(), f"Key {key} is not in the pattern"

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