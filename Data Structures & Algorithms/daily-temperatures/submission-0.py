class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                last_in, last_val = stack.pop()
                result[last_in] = i - last_in
            stack.append([i, t])
        return result