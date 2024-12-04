import re

with open("input.txt") as file:
    data = file.read()



pattern = r"mul\([0-9]+,[0-9]+\)"
pattern1 = r"[0-9]+"

x = re.findall(pattern, data)

val = [re.findall(pattern1, i) for i in x]
val1 = [int(i[0]) * int(i[1]) for i in val]

print(sum(val1))

