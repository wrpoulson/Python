import collections55

def openFile():
    fh = None
    try:
        fh = open("C:/Git/Python/PythonOneHour/lesson_1_input.txt", "r", encoding="ascii")
    except OSError as e:
        print("error %d reading file %s" % (e.errno, e.filename))
        quit()
    return fh

def processFile(fh):
    numWords = 0
    wordFreq = collections.Counter()
    for line in fh:
        words = line.split()
        numWords += len(words)
        for word in words:
            wordFreq[word] += 1
    fh.close()
    return numWords, wordFreq

def printReport(numWords, wordFreq):
    print("\nThere are a total of {0} words".format(numWords))
    for key in sorted(wordFreq.keys()):
        print("key %-12s found %2d times" % (key, wordFreq[key]))

def main():
    fh = openFile()
    (nw, wf) = processFile(fh)
    printReport(nw, wf)

if __name__ == "__main__":
    main()
