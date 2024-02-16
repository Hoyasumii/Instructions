from typing import List
import io

def get_instructions(file: io.TextIOWrapper) -> List[List[str]]:

    output = []
    reject_start = ["//", "#", "\n", "(", ")"]
    line_index = 0

    for line in file.readlines():

        line_index += 1

        rejected = False
        for item in reject_start:
            if line.startswith(item):
                rejected = True
                break
        
        if rejected:
            continue

        if line[-1:] == "\n":
            line = line[:-1]

        if not "(" in line or not ")" in line:
            raise ValueError(f"Invalid syntax at line {line_index}: {line}\n- Expected '(' and ')' in the line\n- Example: command_name(arg1, arg2, arg3)")

        command_name = line[:line.find("(")].strip().lower()
        line = [item.strip() for item in line[line.find("(") + 1:line.rfind(")")].split(",")]

        if len(line) == 1 and line[0] == "":
            line = []
        
        output.append([command_name, *line])

    return output

if __name__=="__main__":
    with open("@instructions", "r", encoding="utf-8") as file:
        print(get_instructions(file))
