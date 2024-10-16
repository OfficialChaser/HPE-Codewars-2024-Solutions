lines = []
with open("input.txt", "r") as f:
    lines = [i for i in f.read().split("\n")]

w = len(lines[0])
h = len(lines)

lines.pop()

output = []

top_str = ""
for _ in range(w):
    top_str += "#"

output.append(top_str)

for i in range(1, h - 2):
    line_str = ""
    counter = 0
    for _ in range(w):
        if counter == 0 or counter == w - 1:
            line_str += "#"
        else:
            line_str += " "
        counter += 1
    output.append(line_str)

bottom_str = ""
for _ in range(w):
    bottom_str += "#"

output.append(bottom_str)

if lines != output:
    for line in output:
        print(line)
else:
    print("Nothing to do.")