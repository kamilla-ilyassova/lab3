class StringManip:
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input()

    def printString(self):
        print(self.s.upper())

str_manip = StringManip()
str_manip.getString()
str_manip.printString()