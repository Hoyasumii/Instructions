def insert(send: str, to: str):
  
	assert isinstance(send, str), "Value must be a string"
	assert isinstance(to, str), "File must be a string"

	try:
		with open(to, "a", encoding="utf-8") as to:
			to.write(send + "\n")
		return True

	except FileNotFoundError:
		return False
	