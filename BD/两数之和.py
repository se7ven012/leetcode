# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

 

# 示例:

# 给定 nums = [2, 7, 11, 15], target = 9

# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]

# 双指针逼近
# 最后的结果可能出现两位数重复，所以用pop弹出
# 然后q结果因为弹出造成的index-1要加回来
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = nums.copy()
        temp.sort()
        i = 0
        j = len(temp)-1
        while i < j:
            if temp[i] + temp[j] < target:
                i = i + 1
            elif temp[i] + temp[j] > target:
                j = j - 1
            else:
                break
        p = nums.index(temp[i])
        nums.pop(p) #弹出该值，为了避免p和q出现重复数值而报错
        q = nums.index(temp[j])
        if q >= p:
            q = q+1
        return[p,q]