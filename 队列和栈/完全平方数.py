# 给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）
# 使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。

# 示例 1:

# 输入: n = 12
# 输出: 3 
# 解释: 12 = 4 + 4 + 4.

# 示例 2:

# 输入: n = 13
# 输出: 2
# 解释: 13 = 4 + 9.

#无脑递归，会超时
class Solution(object):
    def numSquares(self, n):
        square_nums = [i**2 for i in range(1, int(math.sqrt(n))+1)]

        def minNumSquares(k):
            """ recursive solution """
            # bottom cases: find a square number
            # 如果K不在完全平方数组就说明还要多算1步，所以返回1步
            if k in square_nums:
                return 1
            min_step = float('inf')

            # 先从最大的完全平方数拿
            for square in square_nums:
                # 如果k比完全平方数小就跳过下面的步骤
                if k < square:
                    break
                # 开始尝试用新的完全平方数算，如果还是有余数就会再加1步，
                new_step = minNumSquares(k-square) + 1
                # 这里一直取最小的步数
                min_step = min(min_step, new_step)
            return min_step

        return minNumSquares(n)