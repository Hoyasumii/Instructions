import sys

def path_resolve() -> str:
  PATH_STEPS = sys.path[0].split("\\")

  while PATH_STEPS.count("Instructions") < 2:
    PATH_STEPS.append("Instructions")

  while PATH_STEPS.count("Instructions") > 2:
    PATH_STEPS.remove("Instructions")

  PATH_STEPS_REVERSED = PATH_STEPS.copy()
  PATH_STEPS_REVERSED.reverse()
  counter = 0
  
  for path in PATH_STEPS_REVERSED:
    if path != "Instructions":
      counter += 1
    else:
      break

  return "\\".join(PATH_STEPS[:len(PATH_STEPS)-counter])

if __name__=="__main__":
  print(path_resolve())