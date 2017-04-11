fh = open("C:/_repos/Python/PythonOneHour/lesson_1_input.txt", "r", encoding="ascii")
x = 1
numWords = 0
for line in fh:
    print("line {0}: {1}".format(x, line), end="")
    words = line.split()
    numWords = numWords + len(words)
    x += 1
fh.close()
print("\nThere are a total of {0} words".format(numWords))