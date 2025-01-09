
from structures import Stack

def isBalanced(expression):
    stack = Stack(5)
    open = ["(", "[", "{"]
    close = [")", "]", "}"]

    for character in expression:
        if character in open:
            stack.push(character)
        elif character in close:
            if len(stack.list) > 0 and open.index(stack.top()) == close.index(character):
                stack.pop()
            elif len(stack.list) < 1:
                return "Unmatched closing bracket"
            else:
                return "Mismatched brackets"
    
    if len(stack.list) < 1:
        return "All brackets matched and closed"
    else:
        return "Unmatched opening brackets"

print(isBalanced("{}[](]"))