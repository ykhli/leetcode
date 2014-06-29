import Queue
class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string

    @staticmethod
    def dfs(paths, start, end, pathSoFar, foundPaths,explored):
        if start == end:
            foundPaths.append(pathSoFar)
            return 

        for i in paths[start]:
            print start,paths[start]
            pathSoFar.append(i)
            Solution.dfs(paths,i,end,pathSoFar,foundPaths,explored)
            print pathSoFar
            pathSoFar = pathSoFar[0:len(pathSoFar)-3]

    @staticmethod
    def printPaths(paths, start, end, pathSoFar, explored):
        explored.append(start)
        if start == end:
            return pathSoFar.append(start)
        for v in paths[start]:
            if v not in explored:
                pathSoFar.append(v)
                p = Solution.printPaths(paths, v, end, pathSoFar, explored)
                if p: 
                    return p


    def findLadders(self, start, end, dict):
        graph = {}
        dict.append(start)
        dict.append(end)
        # construct the graph
        for word in dict:
            for word2 in dict:
                if word != word2:
                    zipped = zip(list(word), list(word2))
                    numdiff = sum([1 for i in zipped if i[0] != i[1]])
                    if numdiff == 1:
                        if word not in graph: 
                            graph[word] = set([word2])
                        else:
                            graph[word].add(word2)
        #bfs
        visited = []
        q = [start]
        paths = {start:set([])}
        visited = []
        while not q == []:
            v = q.pop(0)
            visited.append(v)
            for neighbor in graph[v]:
                if neighbor not in visited:
                    q.append(neighbor)
                    if v in paths:
                        paths[v].add(neighbor)
                    else:
                        paths[v] = set([neighbor])
        print paths
        #return Solution.printPaths(paths, start, end, [], [])
        res = []
        Solution.dfs(paths,start,end,[start],res,[])
        return res


        
if __name__ == "__main__":
    x = Solution()
    print x.findLadders("hit","cog",["hot","dot","dog","lot","log"])


            

                     

        


