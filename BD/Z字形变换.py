# 将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。

# 比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：

# L   C   I   R
# E T O E S I I G
# E   D   H   N

# 之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。

# 请你实现这个将字符串进行指定行数变换的函数：

# string convert(string s, int numRows);

# 示例 1:

# 输入: s = "LEETCODEISHIRING", numRows = 3
# 输出: "LCIRETOESIIGEDHN"

# 示例 2:

# 输入: s = "LEETCODEISHIRING", numRows = 4
# 输出: "LDREOEIIECIHNTSG"
# 解释:

# L     D     R
# E   O E   I I
# E C   I H   N
# T     S     G

# 这题从例子可得出规律，目标字符串是沿着z字形走动 （行数0至行数max）
# 所以只要写一个循环在每次触底/触头之后反向就行了
# 这里用一个flag就行 flag=1
# if row_counter = 0 or row_counter = max:
#   flag=-flag
# 然后 row_counter += flag

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows<2: return s
        ans = []
        for _ in range(numRows):
            ans.append("")
        row_counter = 0
        flag = -1
        for word in s:
            ans[row_counter] += word
            if row_counter==0 or row_counter==numRows-1:flag = -flag
            row_counter += flag
        return "".join(ans)