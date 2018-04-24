# Balanced Parentheses Check
def balance_check(s):
    if len(s) % 2 != 0:
        return False

    stack = []
    opening = set("([{")
    matches = set([("(", ")"), ("[", "]"), ("{", "}")])

    for paren in s:
        if paren in opening:
            stack.append(paren)
        else:
            if len(stack) == 0:
                return False
            last_open = stack.pop()

            if (last_open, paren) not in matches:
                return False
    return len(stack) == 0


print(balance_check("[][)]"))


def balance_check2(s):
    if len(s) % 2 != 0:
        return False

    stack = []
    lookup = {"(": ")", "{": "}", "[": "]"}

    for paren in s:
        if paren in lookup:
            stack.append(paren)
        else:
            if len(stack) == 0:
                return False
            last_open = stack.pop()

            if lookup[last_open] != paren:
                return False
    return len(stack) == 0


print(balance_check2("[(]"))


####
# Queue to Stacks
class Queue2Stacks(object):
    def __init__(self):
        self.instack = []
        self.outstack = []

    def enqueue(self, element):
        self.instack.append(element)

    def dequeue(self):
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())
        return self.outstack.pop()


head = Queue2Stacks()
head.enqueue(1)
head.enqueue(2)
head.enqueue(3)
print(head.dequeue())
# 1
