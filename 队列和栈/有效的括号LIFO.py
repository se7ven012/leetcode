# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

# 有效字符串需满足：

#     左括号必须用相同类型的右括号闭合。
#     左括号必须以正确的顺序闭合。

# 注意空字符串可被认为是有效字符串。

# 示例 1:

# 输入: "()"
# 输出: true

# 示例 2:

# 输入: "()[]{}"
# 输出: true

# 示例 3:

# 输入: "(]"
# 输出: false

# 示例 4:

# 输入: "([)]"
# 输出: false

# 示例 5:

# 输入: "{[]}"
# 输出: true

# 经典LIFO 
# 若遇左括号则入栈，若遇右括号则将对应的左括号带出
# 遍历完后stack应当为空
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic = {'{': '}',  '[': ']', '(': ')', '?': '?'}
        stack = ['?']
        for c in s:
            # 对于c是左边符号
            # 将该左边符号压入stack
            if c in dic: stack.append(c)
            # 对于c是右边符号
            # 检查该符号是否等于stack最后一位的右边字符, 若不等于,返回False
            # 这里用了pop，意味着每次检查都会把stack最后那位拿掉，如果一切
            # 顺利的话，最后stack就只会剩下一个"?"号。
            # 如果有不匹配的情况会直接返回False
            elif dic[stack.pop()] != c: return False 
        # 这里检查最后stack是否只有一个"?"，是的话就返回True
        return len(stack) ==1


