class PrincipalBuchholz:
    def __init__(self, input):
        if isinstance(input, str):
            self.sequence = input
            self.head, self.argument = self.init_from_string()
        if isinstance(input, tuple):
            assert len(input) == 2
            self.head, self.argument = input
            self.sequence = self.init_from_tuple()
        if isinstance(input, list):
            self.head = input
            self.argument = SumBuchholz([])
            self.sequence = self.init_from_tuple()

    def __str__(self):
        return self.sequence

    def init_from_tuple(self):
        head_string = ""
        for l in self.head:
            if l > 9:
                head_string = f"{head_string}<{l}>"
            else:
                head_string = f"{head_string}{l}"
        if self.argument.sequence == "":
            return head_string
        else:
            return f"{head_string}({self.argument})"

    def init_from_string(self):
        substring = ""
        in_head = True
        in_bracket = False
        head = []
        argument = SumBuchholz("")
        for i, c in enumerate(self.sequence):
            if in_head:
                if c == "(":
                    in_head = False
                elif c == "<":
                    substring = ""
                    in_bracket = True
                elif c == ">":
                    self.head.append(int(substring))
                    in_bracket = False
                elif in_bracket:
                    substring = substring + c
                else:
                    head.append(int(c))
            else:
                argument = SumBuchholz(self.sequence[i:-1])
                break
        return head, argument

    def compare(self, other):
        assert(isinstance(other, PrincipalBuchholz))
        for c1, c2 in zip(self.head, other.head):
            if c1 > c2:
                return 1
            elif c1 < c2:
                return -1
        if len(self.head) == len(other.head):
            return self.argument.compare(other.argument)
        elif len(self.head) > len(other.head):
            rest = SumBuchholz([PrincipalBuchholz((self.head[len(self.head) - len(other.head):], self.argument))])
            return rest.compare(other.argument)
        elif len(self.head) < len(other.head):
            rest_other = SumBuchholz([PrincipalBuchholz((other.head[len(other.head) - len(self.head):], other.argument))])
            return self.argument.compare(rest_other)
class SumBuchholz:
    def __init__(self, input):
        if isinstance(input, str):
            self.sequence = input
            self.sum_list = self.init_from_string()
        if isinstance(input, list):
            self.sum_list = input
            self.init_from_list()

    def __str__(self):
        return self.sequence

    def init_from_string(self):
        sum_list = []
        if self.sequence == "":
            return sum_list
        bracket_count = 0
        last_plus = 0
        for i, c in enumerate(self.sequence + '+'):
            if c == '(':
                bracket_count += 1
            elif c == ')':
                bracket_count -= 1
            elif c == '+' and bracket_count == 0:
                sum_list.append(PrincipalBuchholz(self.sequence[last_plus:i]))
                last_plus = i+1
        return sum_list

    def init_from_list(self):
        self.sequence = ""
        for principal in self.sum_list:
            self.sequence = f"{self.sequence}+{principal.sequence}"
        if len(self.sequence) > 0:
            self.sequence = self.sequence[1:]

    def compare(self, other):
        if len(self.sum_list) == 0 and len(other.sum_list) == 0:
            return 0
        elif len(self.sum_list) == 0 and len(other.sum_list) > 0:
            return -1
        elif len(self.sum_list) > 0 and len(other.sum_list) == 0:
            return 1
        else:
            for p1, p2 in zip(self.sum_list, other.sum_list):
                cmp = p1.compare(p2)
                if cmp != 0:
                    return cmp
            if len(self.sum_list) > len(other.sum_list):
                return 1
            if len(self.sum_list) < len(other.sum_list):
                return -1
            return 0

class bh:
    zero = SumBuchholz("")
    one = SumBuchholz("0")
    two = SumBuchholz("0+0")