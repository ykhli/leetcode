class Solution:
    # @param board, a 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        if board == []:
            return board
        # go through the outmost layer
        uc = set([])
        for row in range(0,len(board)):
            if board[row][0] == 'O':
                uc = uc.union(Solution.bfs(self,row,0,board))
            if board[row][len(board[0])-1] == 'O':
                uc = uc.union(Solution.bfs(self,row,len(board)-1,board))

        for col in range(0,len(board[0])):
            if board[0][col] == 'O':
                uc = uc.union(Solution.bfs(self,0,col,board))
            if board[len(board)-1][col] == 'O':
                uc = uc.union(Solution.bfs(self,len(board)-1,col,board))

        for row in range(0,len(board)):
            for col in range(0,len(board[0])):
                if ((row,col) not in uc) and board[row][col] == 'O':
                    tmp = list(board[row])
                    tmp[col] = 'X'
                    board[row] = "".join(tmp)
        return board

    
    @staticmethod 
    def bfs(self,row,col,board):
        uc = set([])
        visited = []
        q = [(row,col)]
        def neighbors((row,col)):
            neighbors = [(row-1,col),(row+1,col),(row,col-1),(row,col+1)]
            return filter(lambda (x,y): x>=0 and x<len(board) and y>=0 and y<len(board[0]) and board[x][y] == 'O', neighbors)
        
        while q!=[]:
            v = q.pop(0)
            visited.append(v)
            uc.add(v)
            nbs = neighbors(v)
            for n in nbs:
                if n not in visited:
                    q.append(n)
        return uc

if __name__ == "__main__":
    x = Solution()
    #board = [['X','X','X','X'],['X','O','O','X'],['X','X','O','X'],['X','O','X','X']]
    #board = [['O','X','X','O','X'],['X','O','O','X','O'],['X','O','X','O','X'],['O','X','O','O','O'],['X','X','O','X','O']]
    board = ["XOXX","OXOX","XOXO","OXOX","XOXO","OXOX"]
    print x.solve(board)
