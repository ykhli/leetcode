class Solution:
    # @param board, a 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        if board == []:
            return board
        # go through the outmost layer
        rowNum = len(board)
        colNum = len(board[0])
        visited = [[False for i in range(0,colNum)] for j in range(0,rowNum)]
        q = []
        for row in range(0,len(board)):
            if board[row][0] == 'O':
                q.append((row,0))
            if board[row][len(board[0])-1] == 'O':
                q.append((row,len(board[0])-1))

        for col in range(1,len(board[0])):
            if board[0][col] == 'O':
                q.append((0,col))
            if board[len(board)-1][col] == 'O':
                q.append((len(board)-1,col))

        while q:
            v = q.pop(0)
            nbs = Solution.neighbor(board,v[0],v[1])
            # change all reachable 'O's to '$'
            Solution.change(board,v[0],v[1],'$')
            for n in nbs:
                if visited[n[0]][n[1]] == False:
                    q.append(n)
            visited[v[0]][v[1]] = True

        for row in range(0,len(board)):
            for col in range(0,len(board[0])):
                if board[row][col] == '$':
                    Solution.change(board,row,col,'O')
                elif board[row][col] == 'O':
                    Solution.change(board,row,col,'X')
        return board

    @staticmethod
    def neighbor(board,row,col):
        neighbors = [(row-1,col),(row+1,col),(row,col-1),(row,col+1)]
        return filter(lambda (x,y): x>=0 and x<len(board) and y>=0 and y<len(board[0]) and board[x][y] == 'O', neighbors) 

    @staticmethod
    def change(board,row,col,val):
        tmp = list(board[row])
        tmp[col] = val
        board[row] = ''.join(tmp)
    
if __name__ == "__main__":
    x = Solution()
    #board = [['X','X','X','X'],['X','O','O','X'],['X','X','O','X'],['X','O','X','X']]
    #board = [['O','X','X','O','X'],['X','O','O','X','O'],['X','O','X','O','X'],['O','X','O','O','O'],['X','X','O','X','O']]
    board = ["XOXX","OXOX","XOXO","OXOX","XOXO","OXOX"]
    #board = ["OOOOOOOO","OOOOXOOO","OXOOOOOO","OOOOOOOO","XOOXOOXO","OOOOOOOO","OOOOOOOO","OOOOOOOO"]
    print x.solve(board)
