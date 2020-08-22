# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

# 上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Marcos 贡献此图。

# 示例:
# 输入: [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出: 6

# 双指针从两头向中间滤
# 雨水体积 = 两边最大高度 - 当前高度
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        pointer1, pointer2 = 0, len(height) - 1
        maxleft, maxright = height[pointer1], height[pointer2]
        ans = 0

        while pointer1 <= pointer2:
            maxleft = max(height[pointer1], maxleft)
            maxright = max(height[pointer2], maxright)
            if maxleft < maxright:
                ans += maxleft - height[pointer1]
                pointer1 += 1
            else:
                ans += maxright - height[pointer2]
                pointer2 -= 1
        return ans

