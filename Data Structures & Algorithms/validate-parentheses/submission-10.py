class Solution:
    def isValid(self, s: str) -> bool:
        # we want to empty the stack
        # if there is stuff in the stack at the end bad, only want to add open parentheses, if we see a closed, we try to pop
        # ONLY IF IT MATCHES 
        # if there is NO match, we return false

        stack = []
        close = {"}": "{", "]": "[", ")": "("}

        for p in s:
            if stack and p in close:
                if stack[-1] == close[p]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)
        if len(stack) == 0:
            return True
        return False

        