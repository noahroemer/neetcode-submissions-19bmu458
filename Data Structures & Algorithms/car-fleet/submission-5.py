class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        print(cars)
        stack = []

        # stack to track them. go based off of times. once we reach the leading car we pop
        # times must be unique
        # the stack should contain times?

        for pair in cars:
            time = (target - pair[0]) / pair[1]
            print(time)
            if stack and stack[-1] >= time:
                continue
            else:
                stack.append(time)
        return len(stack)