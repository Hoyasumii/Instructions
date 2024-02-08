from typing import Any

class InstanciableDict:
  def __init__(self, **kwargs):
    for key, value in kwargs.items():
      setattr(self, key, value)

if __name__=='__main__':
  my_dict = { "name": "Alberto", "age": 20 }
  id = InstanciableDict(**my_dict)
  print(id.name)