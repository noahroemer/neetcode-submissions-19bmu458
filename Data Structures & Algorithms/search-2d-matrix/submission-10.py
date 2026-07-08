class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # double binary search type of deal
        # first find the correct sub array
        l, r = 0, len(matrix) - 1
        array = []
        while r >= l:
            mid = (r+l)//2
            arr = matrix[mid]
            if (target >= arr[0]) and (target <= arr[-1]):
                array = arr
                break
            elif target < arr[0]:
                r = mid - 1
            elif target > arr[-1]:
                l = mid + 1

        if not array:
            return False
        u, v = 0, len(array) - 1
        while u <= v:
            mid = (u+v)//2
            if target == array[mid]:
                return True
            elif target > array[mid]:
                u = mid + 1
            else:
                v = mid - 1
        return False