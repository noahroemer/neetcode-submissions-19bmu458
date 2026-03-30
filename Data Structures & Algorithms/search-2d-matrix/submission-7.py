class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        arr = None

        # I need to determine which array contains my number
        # i can do this by checking the target with the lower bound of the middle 
        # array as well as the upper bound
        # if it is less, shift down, more, shift up, if it is in the range, reduce to the mid array

        l, r = 0, len(matrix) - 1

        while r >= l:
            mid = (r+l)//2
            if matrix[mid][0] > target:
                r = mid -1
            elif matrix[mid][-1] < target:
                l = mid + 1
            else:
                arr = matrix[mid]
                break

        # perform binary search on the other array
        if arr is None:
            return False
        l1, r1 = 0, len(arr) - 1

        while r1 >= l1:
            m = (r1+l1) // 2
            if target > arr[m]:
                l1 = m + 1
            elif target < arr[m]:
                r1 = m - 1
            else:
                return True
        return False

   