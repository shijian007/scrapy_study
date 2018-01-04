class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s1 = []
        for i in range(len(s)):
            s1.append(s[i])
        temp = {}
        for i in range(len(s1)):
            j = 1
            while j <= i and i+j < len(s1) :
                if s1[i - j] == s1[i + j]:
                    temp[i] = j
                    # print(s[i], s[i + j])
                    j = j + 1
                else:
                    break

        mid = max(temp, key=lambda x: temp[x])
        size = temp.get(mid)

        start = mid - size
        end = mid + size + 1
        s2 = s1[start: end]
        str = ('').join(s2)
        return str


if __name__=="__main__":
    s = 'bcabacdcab'
    P = Solution()
    print(P.longestPalindrome(s))


