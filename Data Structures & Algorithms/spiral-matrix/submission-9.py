class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # let's track the start
        # once we reach the start, then we go in
        l, r = 0, len(matrix[0]) - 1
        t, b = 0, len(matrix) - 1
        res = []
        i = 0

        while r >= l and b >= t:
            start = matrix[l][t]
            res.append(start)
            while i < r:   # going top row
                i += 1
                res.append(matrix[t][i])
            i = t
            while i < b:
                i += 1
                res.append(matrix[i][r])
            i = r
            while i > l and t != b:
                i -= 1
                res.append(matrix[b][i])
            i = b
            while i > (t+1) and r != l:
                i -= 1
                res.append(matrix[i][l])
            l += 1
            r -= 1
            t += 1
            b -= 1
            i = l
        return res
            
            