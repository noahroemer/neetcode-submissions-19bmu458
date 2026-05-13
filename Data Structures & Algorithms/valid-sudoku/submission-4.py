class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowdict = defaultdict(set)
        coldict = defaultdict(set)
        sqdict = defaultdict(set)

        for row in range(len(board)):
            for i in range(len(board)):
                if board[row][i] in rowdict[row] and board[row][i] != ".":
                    return False
                if board[i][row] in coldict[row] and board[i][row] !=  ".":
                    return False
                
                if board[row][i] in sqdict[(row//3,i//3)] and board[row][i] != ".":
                    return False                
                
                sqdict[(row//3,i//3)].add(board[row][i])

                
                rowdict[row].add(board[row][i])
                coldict[row].add(board[i][row])
        return True
            
                
                
  
 