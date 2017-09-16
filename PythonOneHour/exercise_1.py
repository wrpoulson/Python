import collections

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
    wordIndex = collections.defaultdict(set)
    lineNum = 0
    for line in fh:
        lineNum += 1
        words = line.split()
        numWords += len(words)
        for word in words:
            wordFreq[word] += 1
            wordIndex[word].add(str(lineNum))
    fh.close()
    return (numWords, wordFreq, wordIndex)

def printReport(stats):
    (numWords, wordFreq, wordIndex)= stats
    print("\nThere are a total of {0} words".format(numWords))
    for key in sorted(wordFreq.keys()):
        print("key %-12s found %2d times" % (key, wordFreq[key]))
    for key in sorted(wordIndex.keys()):
        print("key %-12s found on lines: %s" % (key, ",".join(wordIndex[key])))

def main():
    fh = openFile()
    stats = processFile(fh)
    printReport(stats)

if __name__ == "__main__":
    main()
