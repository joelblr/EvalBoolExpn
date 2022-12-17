# -*- coding: utf-8 -*-


"""
    Displays Truth Table for a given Valid Boolean Expression.

    F = A.b + B.a

     A │ B │ Y
    ───┼───┼─── 
     0 │ 0 │ 0
     0 │ 1 │ 1
     1 │ 0 │ 1
     1 │ 1 │ 0

    a :- compliment of A, (ie, A')
"""


class BoolExpn :

    unique = {}
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
        k = 0
        for ch in self.infix :

            if ch.isspace() :
                continue

            elif ch.isalpha() :
                BoolExpn.postfix += ch
                if ch.upper() not in BoolExpn.unique :
                    BoolExpn.unique[ch.upper()] = k
                    k += 1

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
        # dict{var : idx, ..},  idx : 0, 1, 2..... for TT order
        ''' dict{'a' : 1, 'A' : 0, 'B' : 1, 'C' : 0, ...} '''
        self.getInfix()
        self.in2postfix()



"""
    USE a as !A
"""
class TruthTable :

    def __init__(self) :
        self.unique = BoolExpn.unique
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
                if ch.islower() :
                    stac.append( (self.BoolInput[self.unique[ch.upper()]])^1)
                else :
                    stac.append(self.BoolInput[self.unique[ch]])
            else :
                y = stac.pop()
                if ch == '!' :
                    stac.append(self.compute(y, ch, -1))
                else :
                    x = stac.pop()
                    stac.append(self.compute(x, ch, y))
        return stac.pop()


    def printTable(self) :

        for i in self.unique :
            print(" %c │" % i, end = "")
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
    
    
    
