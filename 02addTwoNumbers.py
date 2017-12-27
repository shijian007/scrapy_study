# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        len1 = len(l1)-1
        s1 = 0
        while(len1 >= 0):
            s1 = l1[len1]*(10**(len1)) + s1
            len1 = len1-1

        len2 = len(l2)-1
        s2 = 0
        while(len2 >= 0):
            s2 = l2[len2]*(10**(len2)) + s2
            len2 = len2-1

        sum1 = s1+s2
        tmp = str(sum1)
        sum = list(tmp)
        lensum = len(sum)

        print(sum)
        for i in range(lensum):
            print(sum[lensum-i-1],'\n')

if __name__=='__main__':
    l1 = [2,4,7,3]
    l2 = [3,1,6]
    S = Solution()
    S.addTwoNumbers(l1,l2)