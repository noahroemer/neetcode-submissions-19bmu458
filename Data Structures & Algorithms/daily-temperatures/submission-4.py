class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # store index for days and temperature 
        # we should have a stack of the temperature and the index

        temps = [[i, t] for i, t in enumerate(temperatures)]
        stack = []
        res = [0]*len(temperatures)

        # append to the stack after we check for everything
        for pair in temps:
            while stack and (pair[1] > stack[-1][1]):
                res[stack[-1][0]] += pair[0] - stack[-1][0]
                stack.pop()

            stack.append(pair)
        return res

            

 

        