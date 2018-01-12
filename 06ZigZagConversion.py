class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        s1 = list(s)
        # 每组元素个数
        n = numRows + numRows - 2
        # 最后一组，余数
        b = len(s1) % n
        if b > 0:
            for i in range(n - b):
                s1.append('%')
        # 组数，整数
        a = int(len(s1) / n)
        #每组数据
        k = []
        # 每排的数据
        rowdata = []
        if len(s) > numRows:
            if numRows > 1:
                for i in range(a):
                    k.append(s1[i * n: i * n + n])

        #j是每组数据长度
        for j in range(len(k[0])):
            if j == 0:
                for i in range(a):
                    rowdata.append(k[i][0])
            if j >0 and j < len(k[0])-2:
                #第i组，a是组数
                for i in range(a):
                    rowdata.append(k[i][j])
                    rowdata.append(k[i][j+numRows-1])

            if j == numRows - 1:
                for i in range(a):
                    rowdata.append(k[i][j])

        numk = []
        for i in rowdata:
            if i != "%":
                numk.append(i)
        rowdata = ('').join(numk)
        return rowdata
        #PAHNAPLSIIGYIR


if __name__=="__main__":
    # s = 'qwertyuiopaszxcv'
    s = 'PAYPALISHIRING'
    P = Solution()
    print(P.convert(s, 3))