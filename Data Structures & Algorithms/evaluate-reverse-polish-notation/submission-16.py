import math 
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        # here is a stack problem as well. when we see the operator, we pop the last two numbers and perform the operation 
        # and track the res

        stack = []
        res = 0

        for item in tokens:
            if item == "+":
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(val1 + val2)
            elif item == "-":
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(val2-val1)
            elif item == "*":
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(val1*val2)
            elif item == "/":
                val1 = stack.pop()
                val2 = stack.pop()
                if val2 / val1 >= 0:
                    stack.append(val2//val1)
                else:
                    stack.append(math.ceil(val2/val1))

            else:
                stack.append(int(item))
            print(stack)
        return stack[-1] 
        

