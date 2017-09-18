import collections

class docIndexer:
    def __init__(self):
        pass

    def openFile(self, filename):
        self.fh = None
        try:
            self.fh = open(filename, "r", encoding="ascii")
        except OSError as e:
            print("error %d reading file %s" % (e.errno, e.filename))
            return False
        return True

    def processFile(self):
        numWords = 0
        wordFreq = collections.Counter()
        wordIndex = collections.defaultdict(set)
        lineNum = 0
        for line in self.fh:
            lineNum += 1
            words = line.split()
            numWords += len(words)
            for word in words:
                wordFreq[word] += 1
                wordIndex[word].add(str(lineNum))
        self.fh.close()
        self.stats = (numWords, wordFreq, wordIndex)

    def printReport(self):
        (numWords, wordFreq, wordIndex)= self.stats
        print("\nThere are a total of {0} words".format(numWords))
        for key in sorted(wordFreq.keys()):
            print("key %-12s found %2d times" % (key, wordFreq[key]))
        for key in sorted(wordIndex.keys()):
            print("key %-12s found on lines: %s" % (key, ",".join(wordIndex[key])))

def main():
    di = docIndexer()
    if di.openFile("/home/pi/git/Python/PythonOneHour/lesson_1_input.txt"):
        di.processFile()
        di.printReport()

if __name__ == "__main__":
    main()
