# 给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。

# 说明:
# 初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
# 你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。

# 示例:
# 输入:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3

# 输出: [1,2,2,3,5,6]

# 双指针最小空间复杂度
# 双指针分别指向两个nums，直接从nums1最后一个元素开
# 始赋值对比两个指针指向的值，谁大就放在最后一个元素
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        # 取值用的指针
        pointer1 = m - 1
        pointer2 = n - 1
        # 赋值用的指针
        p = m + n - 1

        while pointer1 >= 0 and pointer2 >= 0:
            if nums1[pointer1] < nums2[pointer2]:
                nums1[p] = nums2[pointer2]
                pointer2 -= 1
            else:
                nums1[p] = nums1[pointer1]
                pointer1 -= 1
            p -= 1

        # 如果指针1先走完（pointer1<0），nums2里还剩余元素
        # 此时nums2里的元素都比nums1里最小的元素小
        # 所以直接吧nums2里的元素加在nums1里
        # 因为nums1的长度可以装下nums2
        # 所以直接按nums2的指针位添加进nums1就行
        nums1[: pointer2 + 1] = nums2[: pointer2 + 1]

