alphabet = {}

#instruction set = (state1, if this, then this, state2)
instructions = {}

class Tape:
    def __init__(self):
        self.tape = []

    def addSym(self, symbol):
        self.tape.append(symbol)
        
    def printTape(self):
        for s in self.tape:
            print(str(s), end = " ")
#print(instructions)

class Head:
    def __init__(self):
        pass


    def read(self):
        pass

    def write(self):
        pass

    def erase(self):
        pass

    
        

tape = Tape()
tape.addSym("a")
tape.addSym("b")
tape.printTape()
