# 盛最多水的容器

# 给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
# 在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。
# 找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
# 说明：你不能倾斜容器，且 n 的值至少为 2。

# 示例：
# 输入：[1,8,6,2,5,4,8,3,7]
# 输出：49

# 这是一道十分简单的双指针题
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        counter = len(height) - 1
        water = 0
        while left < right:
            water = max(water, min(height[left], height[right]) * counter)
            counter -= 1
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return water
