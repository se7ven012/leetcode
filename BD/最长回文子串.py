# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

# 示例 1：
# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。

# 示例 2：
# 输入: "cbbd"
# 输出: "bb"

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 写中心扩散函数
        def spread(l,r,s):
            while (l>=0 and r<len(s) and s[l] == s[r]):
                l -= 1
                r += 1
            return s[l+1:r]

        # 计算部分， 这里我们只能迭代s以itr为中心一次次向外扩散试出最长值
        length = len(s)
        if len(s)==0: return ""
        ans = s[0]
        for itr in range(length-1):
            even = spread(itr,itr,s)
            odd = spread(itr,itr+1,s)
            if max(len(even),len(odd)) > len(ans):
                ans = even if len(even)>len(odd) else odd
        return ans
