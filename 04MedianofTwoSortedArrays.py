class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        a = nums1[:]
        b = nums2[:]
        for i in b:
            a.append(i)
        a.sort()

        print(a)
        if len(a)%2 == 0:
            return 0.5*(a[int(len(a)/2-1)] + a[int(len(a)/2)])
        else:
            return a[int(len(a)/2-0.5)]


if __name__=="__main__":
    nums1 = [1,3]
    nums2 = [2]
    P = Solution()
    print(P.findMedianSortedArrays(nums1,nums2))

