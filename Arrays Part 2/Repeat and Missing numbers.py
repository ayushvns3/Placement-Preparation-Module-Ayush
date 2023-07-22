class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        A = list(A)
        for i in range(1,len(A)+1):
            if i in A:
                A.remove(i)
            else:
                A.append(i)   
        return A
        