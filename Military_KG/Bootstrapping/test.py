class Solution:
    def jiecheng(self, n):
        result = 1
        for i in range(1, n + 1):
            result = result * i
        return result

    def climbStairs(self, n):
        result = 0
        if n == 1:
            return (1)
        if n == 2:
            return (2)
        else:
            if (n % 2) != 0:
                k = int((n - 1) / 2)
            if (n % 2) == 0:
                k = int(n / 2)
            for j in range(1, k + 1):
                result = result + int(self.jiecheng(j + n - 2 * j) / (self.jiecheng(j) * self.jiecheng(n - 2 * j)))
            result = result + 1
            return (result)
