class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowdict = defaultdict(set)
        coldict = defaultdict(set)
        corndict = defaultdict(set)
        
        for r in range(len(board)):
            for c in range(len(board)):
                if board[r][c] == ".":
                    continue
                if board[r][c] in rowdict[r]:
                    return False
                elif board[r][c] in coldict[c]:
                    return False
                elif board[r][c] in corndict[(r//3, c//3)]:
                    return False
                else:
                    coldict[c].add(board[r][c])
                    rowdict[r].add(board[r][c])
                    corndict[(r//3, c//3)].add(board[r][c])
        return True
                
                
