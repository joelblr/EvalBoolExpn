# -*- coding: utf-8 -*-


"""
    To Display Truth Table for a given Valid Boolean Expression.
    F = A.a + B.b

    a :- compliment of A, (ie, A')
"""


class BoolExpn :

    unique = set()
    postfix = ''
    def __init__(self) :
        self.infix = '('


    def prior(self, ch) :
        if ch in {'('} :
            return 1
        elif ch in {'+'} :
            return 2
        elif ch in {'^'} :
            return 3
        elif ch in {'.'} :
            return 4
        elif ch in {'!'} :
            return 5


    def getInfix(self) :
        self.infix += input("ENTER A BOOLEAN EXPRESSION: ") + ')'
        print()


    def in2postfix(self) :

        stack = []
        for ch in self.infix :

            if ch.isspace() :
                continue

            elif ch.isalpha() :
                BoolExpn.postfix += ch
                BoolExpn.unique.add(ch.upper())

            elif ch in {'(', '!'} :
                stack.append(ch)

            elif ch == ')' :
                while stack[-1] != '(' :
                    BoolExpn.postfix += stack.pop()
                stack.pop()

            else :
                while self.prior(stack[-1]) >= self.prior(ch) :
                    BoolExpn.postfix += stack.pop()
                stack.append(ch)


    def run(self) :
        ''' dict{'a' : 1, 'A' : 0, 'B' : 1, 'C' : 0, ...} '''
        self.getInfix()
        self.in2postfix()



"""
    TODO : USE a as !A
"""
class TruthTable :

    def __init__(self) :
        self.key = 65
        self.N = len(BoolExpn.unique)
        self.BoolInput = [0 for i in range(self.N)]
        self.postfix = BoolExpn.postfix


    def nextInput(self) :
        for idx in range(self.N-1, -1, -1) :
            self.BoolInput[idx] ^= 1
            if self.BoolInput[idx] :
                return


    def compute(self, x, op, y) :

        if op in {'!'} :
            return x^1
        if op in {'+'} :
            return x | y
        if op in {'^'} :
            return x ^ y
        if op in {'.'} :
            return x & y


    def evalBoolExpn(self) :
        stac = []
        for ch in self.postfix :
            if ch.isalpha() :
                stac.append(self.BoolInput[ord(ch) - self.key])
            else :
                y = stac.pop()
                if ch == '!' :
                    stac.append(self.compute(y, ch, -1))
                else :
                    x = stac.pop()
                    stac.append(self.compute(x, ch, y))
        return stac.pop()


    def printTable(self) :

        for i in range(self.N) :
            print(" %c │" % chr(self.key + i), end = "")
        print(" Y")
        print(f'{"───┼" * (self.N)}─── ')

        for k in range(1<<self.N) :
            for ch in self.BoolInput :
                print(" %d │" % ch, end = "")
            print(" %d" % self.evalBoolExpn())
            self.nextInput()

        return


if __name__ == '__main__':
    BoolExpn().run()
    TruthTable().printTable()
    
    
    
