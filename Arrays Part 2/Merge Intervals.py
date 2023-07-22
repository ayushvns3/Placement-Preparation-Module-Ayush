class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        i=0
        intervals.sort()
        res = [intervals[0]]
        for i, j in intervals[1:]:
            end = res[-1][1]
            
            if end >= i:
                res[-1][1] = max(res[-1][1],j)
            else:
                res.append([i,j])
        return res