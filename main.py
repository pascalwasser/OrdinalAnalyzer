class buchholz:
    def __init__(self, input):
        if isinstance(input, str):
            self.seq = input
            self.ord = self.getOrd()
        if isinstance(input, list):
            self.ord = input
            self.seq = self.getSeq()

    def __str__(self):
        return self.seq

    def getSeq(self):
        self.seq = ""


    def getOrd(self):
        if self.seq == "":
            return []
        sum = self.splitSum()
        ord = [self.splitArgument(s) for s in sum]
        return ord
    def succ(self):
        if len(self.seq) == 0:
            return buchholz("0")
        return buchholz(f"{self}+0")

    def getFundamental(self, n):
        if self.seq == '':
            return []
        if self.seq == "0":
            return ["" for i in range(n)]
        if len(self.seq) == 1:
            fun = []
            fb = buchholz("")
            for i in range(n):
                fun.append(fb)
                fb = fb.succ()
            return fun
        if self.seq[-2:] == "+0":
            return [self.seq[:-2] for i in range(n)]
        splitSum = self.splitSum()
        if len(splitSum) > 1:
            pfunda = buchholz(splitSum[-1]).getFundamental(n)
            part = ""
            for s in splitSum[:-1]:
                part = part+s
            fun = [f"{part}+{f}" for f in pfunda]
            if fun[0][-1] == '+':
                fun[0] = fun[0][:-1]
            return fun
        if self.seq[0].isdigit() and self.seq[1] == '(' and self.seq[-1] == ')':
            arg = buchholz(self.seq[2:-1])
            splitArg = arg.splitSum()
            if len(splitArg) > 1 and splitArg[-1] == "0":
                subarg = arg.seq[:-2]
                funda = []
                next = f"{self.seq[0]}({subarg})"
                for i in range(n-1):
                    funda.append(next)
                    next = f"{next}+{self.seq[0]}({subarg})"
                return funda[0:n]
        return ['']

    def getFundaString(self, n):
        funda = self.getFundamental(n)
        return listToString(funda)

    def splitSum(self):
        open = 0
        splits = [-1]
        for i, c in enumerate(self.seq):
            if c == '(':
                open += 1
            if c == ')':
                open -= 1
            if c == '+' and open == 0:
                splits.append(i)
        splitSeq = []
        for i in range(len(splits)-1):
            splitSeq.append(self.seq[(splits[i]+1):splits[i+1]])
        splitSeq.append(self.seq[(splits[-1]+1):])
        return splitSeq

    def splitArgument(self, ordinal):
        funcList = []
        rest = buchholz("")
        for i, c in enumerate(ordinal):
            if c.isdigit():
                funcList.append(int(c))
            elif c == '(':
                rest = buchholz(ordinal[i+1:-1])
                break
        return (funcList, rest.getOrd())

    def compare(self, other):
        selfm = self.splitSum()[0]
        otherm = other.splitSum()[0]
        return buchholz(selfm).comparem(otherm)

    def comparem(self, otherm):
        for i in range(max(len(self.seq), len(otherm))):
            if self.seq[i] == "(":
                return False

def listToString(list):
    return [l.__str__() for l in list]

if __name__ == '__main__':
    # complex = SumBuchholz("01(0+0)+0(0(01+001)+0+0)")
    #prince = PrincipalBuchholz("01(0+0)")
    zero = SumBuchholz([])
    one = SumBuchholz([PrincipalBuchholz(([0]))])
    # prince = PrincipalBuchholz(([0,1], SumBuchholz([one, one])))
    # copy_prince = PrincipalBuchholz(prince.sequence)
    # double_copy_prince = PrincipalBuchholz((copy_prince.head, copy_prince.argument))

    # copy_complex = SumBuchholz(complex.sum_list)
    #one = SumBuchholz("00+0")
    #one = buchholz("00")
    one.compare(one)
    print(1)
    # print(prince)
    #print(one.getFundaString(5))

