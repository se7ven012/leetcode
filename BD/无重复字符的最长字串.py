# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

# 示例 1:

# 输入: "abcabcbb"
# 输出: 3 
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

# 示例 2:

# 输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

# 示例 3:

# 输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = ''
        tep = ''
        for i in s:
            # 如果temp里没有就加上i
            if i not in tep:
                tep += i
            # 如果temp里有，就把那一位前面所有的值都消掉
            # 再加上i
            else:
                tep = tep[tep.index(i)+1:]
                tep += i
            # 如果temp长度超过answer，就更新answer   
            if len(tep) > len(ans): 
                ans = tep 
        return len(ans)