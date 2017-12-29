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
        sorted(a)

        print(a)
        if len(a)%2 == 0:
            print(0.5*(a[int(len(a)/2-1)] + a[int(len(a)/2)]))
        else:
            print(a[int(len(a)/2-0.5)])


if __name__=="__main__":
    nums1 = [1,2,5,7]
    nums2 = [8,9,89]
    P = Solution()
    P.findMedianSortedArrays(nums1,nums2)

