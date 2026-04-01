import math 
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # do math... 

        # input is a string
        # we do in left to right order
        stack = []
        # add to stack if not operator
        # if operator, perform a operation on total and stack values
        # there is an edge case at the beginning
        for c in tokens:
            if c == "+":
                stack[-2] = stack[-1] + stack[-2]
                stack.pop()

            elif c == "-":
                stack[-2] = stack[-2] - stack[-1]
                stack.pop()

            elif c == "*":
                stack[-2] = stack[-1] * stack[-2]
                stack.pop()
            elif c == "/":
                stack[-2] = math.trunc(stack[-2] / stack[-1])
                stack.pop()
                # do this for all 4 operators
            else:
                # here we are appending the numbers
                stack.append(int(c))
            print(stack)

        return int(stack[0])
        