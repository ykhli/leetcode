# Definition for a point
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        maxNum = 0
        if len(points) <= 2:
            return len(points)

        for pt1 in range(0,len(points)):
            s = {}
            # Counting duplication. Starts from 1 since we need to count the starting point as well. 
            dup = 1
            for pt2 in range(0,len(points)):
                # Counting duplication
                if (points[pt1].x == points[pt2].x and points[pt1].y == points[pt2].y and pt1 != pt2):
                    dup += 1 
                # Get rid of pt1 in this iteration
                elif pt1 != pt2 :
                    # Take care of 0 denominator case
                    if points[pt1].x - points[pt2].x == 0:
                        if 'v' in s:
                            s['v'] += 1
                        else:
                            s['v'] = 1
                    elif points[pt1].y - points[pt2].y == 0:
                        if 'h' in s:
                            s['h'] += 1
                        else:
                            s['h'] = 1
                    else:
                        # Store slopes in a dictionary
                        slope = float( points[pt1].y - points[pt2].y)/(points[pt1].x - points[pt2].x)
                        if slope in s:
                            s[slope] += 1
                        else:
                            s[slope] = 1
              
                # Find max
                if (len(s) > 0):
                    maxNum = max(maxNum, max(s.values())+dup)
                else:
                    maxNum = max(maxNum, dup)
                        
       
        return maxNum


if __name__ == "__main__":
    x = Solution()
    print x.maxPoints([(0,0),(0,1)])

