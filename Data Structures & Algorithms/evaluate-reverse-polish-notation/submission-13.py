import math 
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for num in tokens:
            if num == "+":
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(val1 + val2)

            elif num == "-":
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(val2-val1)

            elif num == "*":
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(val1*val2)

            elif num == "/":
                val1 = stack.pop()
                val2 = stack.pop()
                if (val2/val1) >= 0:
                    stack.append(val2//val1)
                else:
                    stack.append(math.ceil(val2/val1))

                



            else:
                stack.append(int(num))
            print(stack)

        return stack[0]

        
        