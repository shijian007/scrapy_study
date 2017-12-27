#--coding='utf-8'--

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        i = 1
        k = 0
        n=[0,0,0,0]

        while(i<len(nums)):
            j=1
            while(j<len(nums)):
                if i!=j:
                    if nums[i]+nums[j] == target:
                        n[k] = i
                        n[k+1] = j
                        k=+2
                        # print(n)
                j = j+1
            i = i+1
        print(n)
        if (n[0]==n[3]) and (n[1]==n[2]):
            print(n[0],n[1])
        return n[0],n[1]


# if __name__=='__main__':
    # print("请输入数组:\n")
    # nums = input()
    # # nums = list(nums)
    # print(nums)
    # print("请输入目标值:\n")
    # target = input()
    # # target = list(target)
    # print(target)
    #
    # nums = [2,4,6,8,10,12]
    # target = 20
    # s = Solution()
    # s.twoSum(nums,target)

