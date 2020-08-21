# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

# 说明：本题中，我们将空字符串定义为有效的回文串。

# 示例 1:
# 输入: "A man, a plan, a canal: Panama"
# 输出: true

# 示例 2:
# 输入: "race a car"
# 输出: false


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        p1 = 0
        p2 = len(s)-1
        while p1 < p2:
            # 左指针指到非数字/字符
            while p1 < p2 and not s[p1].isalnum():
                p1 += 1
            # 右指针指到非数字/字符
            while p1 < p2 and not s[p2].isalnum():
                p2 -= 1
            if p1 < p2:
                if s[p1].lower() != s[p2].lower():
                    return False
                p1 += 1
                p2 -= 1
        return True
