import os

FILENAME = "lecture_demonstration.py"

if os.path.exists(FILENAME):
    with open(FILENAME, "r") as f:
        for line in f:
            print(line, end="")
else:
    print(FILENAME, "does not exist")

os.remove("data2.txt")

