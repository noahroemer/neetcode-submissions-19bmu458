class Solution:
    def tribonacci(self, n: int) -> int:

        zero, one, two = 0, 1, 1

        for num in range(n):
            temp = two
            two = zero + one + two
            zero = one
            one = temp
        return zero
        