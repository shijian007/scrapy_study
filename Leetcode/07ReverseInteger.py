class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x1 = str(x)
        xx = list(x1)

        # if x1.find('1'):
        #     if x1.find('2') and x1.find('3') and x1.find('4') and x1.find('5') and x1.find(
        #         '6') and x1.find('7') and x1.find('8') and x1.find('9'):
        #
        #         print('bbbbbbbbbbbbbb')

        if x > 0:
            for i in range(int(len(xx) / 2)):
                if len(xx) - i - 1 >= i:
                    temp = xx[i]
                    xx[i] = xx[len(xx) - i - 1]
                    xx[len(xx) - i - 1] = temp
            # print(xx)
            xx = ('').join(xx)
            xs = int(xx)
            return xs

        if x < 0:
            for i in range(int((len(xx)-1) / 2)):
                if len(xx) - i - 1 >= i:
                    temp = xx[i + 1]
                    xx[i + 1] = xx[len(xx) - i - 1]
                    xx[len(xx) - i - 1] = temp
            print(xx)
            xx = ('').join(xx)
            xs = int(xx)
            return xs

        if x ==0:
            return





if __name__=="__main__":

    x = 123456789
    P = Solution()
    print(P.reverse(x))