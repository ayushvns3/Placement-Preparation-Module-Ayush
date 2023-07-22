class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        list(A)
        count = 0
        if B in A:
           count += 1
        for i in range(len(A)):
            xor = A[i]
            for j in range(i+1,len(A)):
                xor = xor^A[j]
                if xor == B:
                    count += 1
        return count