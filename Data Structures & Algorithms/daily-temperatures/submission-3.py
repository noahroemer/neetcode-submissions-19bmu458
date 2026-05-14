class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # store index for days and temperature 

        temps = [[temperatures[i], i] for i in range(len(temperatures))]
        stack = []
        res = [0]*len(temperatures)

        for pair in temps:
            while stack and stack[-1][0] < pair[0]:
                res[stack[-1][1]] = pair[1] - stack[-1][1]
                stack.pop()
            stack.append(pair)
        return res


 

        