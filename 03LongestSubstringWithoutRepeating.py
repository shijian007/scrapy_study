class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        #-----------------自己写的,未起效-------------
        # a = list(s)
        # len1 = len(a)
        # print(len1)
        # i = 0
        # k = 0
        # n = []
        # m = []
        # while i < len1:
        #     j = i+1
        #     while j < len1:
        #         if a[i] ==a[j]:
        #             n[k] = i
        #             m[k] = j
        #             k = k+1
        #             print(i,j)
        #         else:
        #             j = j+1
        #
        #     i = i+1
        # print(n)
        # return n,m


        #---------------使用find()函数---------------------
        # lls = 1
        # if len(s) == 0:
        #     return 0
        # if len(s) == 1:
        #     return 1
        # i = 1
        # curbegin = 0
        # while i < len(s):
        #     cur = s.find(s[i],curbegin,i)
        #     if cur != -1:
        #         lls = max(lls,i - curbegin)
        #         curbegin = cur + 1
        #     i += 1
        # if s.find(s[len(s) - 1],curbegin,len(s) - 1) == -1:
        #     return max(lls,len(s) - curbegin)
        # return lls

        #------------使用enumerate(),反用字典-----------------
        res = 0
        left = 0
        d = {}

        for i, ch in enumerate(s):
            if ch in d and d[ch] >= left:
                left = d[ch] + 1
            d[ch] = i
            res = max(res, i - left + 1)
        return res


if __name__=="__main__":
    s = 'pwkewiuahetv'
    h = Solution()

    print(h.lengthOfLongestSubstring(s))