class FileHandling:
    def writeFile(self, file1, file2):
        x = open(file1, "r")
        y = open(file2, "w")

        y.write(x.read())

    def appendFile(self, file1, file2):
        x = open(file1, "r")
        y = open(file2, "a")

        y.write(x.read())

    def readFile(self, file1):
        x = open(file1, "r")
        print(x.read())


if __name__ == '__main__':
    FileHandling.appendFile(__name__, "f1.txt", "f2.txt")
    FileHandling.writeFile(__name__, "f1.txt", "f2.txt")
    FileHandling.readFile(__name__, "file.txt")
