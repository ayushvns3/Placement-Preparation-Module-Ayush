class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pivot=0
        res=0
        count=set()
        for i in range(len(s)):
            while s[i] in count:
                count.remove(s[pivot])
                pivot += 1
            count.add(s[i])
            res = max(res, i-pivot+1)
        return res
        