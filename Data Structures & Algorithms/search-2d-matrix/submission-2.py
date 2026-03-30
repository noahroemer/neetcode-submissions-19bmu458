class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        hawk_ray = None

        a = 0
        b = len(matrix) - 1
        
        while b >= a:
            m = a + (b-a)//2
            if target < matrix[m][0]:
                b = m - 1
            elif target > matrix[m][-1]:
                a = m + 1
            else: 
                hawk_ray = matrix[m]
                break
        if hawk_ray == None:
            return False


        l = 0
        r = len(hawk_ray) - 1
        while r >= l:
            m = l + (r-l)//2
            if target > hawk_ray[m]:
                l = m + 1
            elif target < hawk_ray[m]:
                r = m - 1
            else:
                return True
        return False