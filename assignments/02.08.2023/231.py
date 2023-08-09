class Solution(object):
    def isPowerOfTwo(self, n):
        def pow(n):
            if n ==1:
                return True
            if n%2 != 0 or n<=0: 
                return False
            return pow(n/2)
        return pow(n)