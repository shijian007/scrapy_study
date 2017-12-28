class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        a = list(s)
        len1 = len(a)
        print(len1)
        i = 0
        k = 0
        n = []
        m = []
        while i < len1:
            j = i+1
            while j < len1:
                if a[i] ==a[j]:
                    n[k] = i
                    m[k] = j
                    k = +1
                    print(i,j)
                else:
                    j = +1

            i = +1
        print(n)
        return n,m

if __name__=="__main__":
    s = 'abcnmcpa'
    h = Solution()

    print(h.lengthOfLongestSubstring(s))