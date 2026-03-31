class Solution:
    def isValid(self, s: str) -> bool:
        #stack

        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }
        
        
        for p in s:
            if stack and p in closeToOpen and closeToOpen[p] == stack[-1]:
                stack.pop()

            else:
                stack.append(p)
        if stack:
            return False
        else:
            return True
        
        
            