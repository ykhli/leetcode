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
        visited = [[False for i in xrange(0,colNum)] for j in xrange(0,rowNum)]
        q = []
        for row in xrange(0,len(board)):
            if board[row][0] == 'O':
                q.append((row,0))
            if board[row][len(board[0])-1] == 'O':
                q.append((row,len(board[0])-1))

        for col in xrange(1,len(board[0])):
            if board[0][col] == 'O':
                q.append((0,col))
            if board[len(board)-1][col] == 'O':
                q.append((len(board)-1,col))

        while q:
            v = q.pop(0)
            q += Solution.neighbor(visited,board,v[0],v[1])
            # change all reachable 'O's to '$'
            if board[v[0]][v[1]] == 'O':
                board[v[0]][v[1]] = '$'
            visited[v[0]][v[1]] = True

        for row in xrange(0,len(board)):
            for col in xrange(0,len(board[0])):
                if board[row][col] == '$':
                    board[row][col] = 'O'
                elif board[row][col] == 'O':
                    board[row][col] = 'X'
        return board

    @staticmethod
    def neighbor(board,row,col):
        neighbors = [(row-1,col),(row+1,col),(row,col-1),(row,col+1)]
        return filter(lambda (x,y): x>=0 and x<len(board) and y>=0 and y<len(board[0]) and board[x][y] == 'O' and visited[row][col] == False, neighbors) 

