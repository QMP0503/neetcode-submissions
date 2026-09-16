class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = {} 
        col = {}
        sqr = {} #co-ordinates // 3 gets you square location

        #grid fixed to 9x9
        for i in range(9):
            for j in range(9):
                value = board[i][j] 
                if value == ".":
                    continue
                if( 
                    value in row.get(i, set())
                    or value in col.get(j, set())
                    or value in sqr.get((i//3, j//3), set())
                ):
                    return False
                
                currRow = row.setdefault(i, set())
                currCol = col.setdefault(j, set())
                currSqr = sqr.setdefault((i//3, j//3), set())

                currRow.add(value)
                currCol.add(value)
                currSqr.add(value)
        
        return True


                