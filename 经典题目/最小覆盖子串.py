# 给你一个字符串 S、一个字符串 T 。请你设计一种算法，可以在 O(n) 的时间复杂度内，从字符串 S 里面找出：包含 T 所有字符的最小子串。


# 示例：
# 输入：S = "ADOBECODEBANC", T = "ABC"
# 输出："BANC"


# 提示：
#     如果 S 中不存这样的子串，则返回空字符串 ""。
#     如果 S 中存在这样的子串，我们保证它是唯一的答案。

#%%
# 做字典
def def_value():
    return "Not Present"


d = collections.defaultdict(def_value)
d["a"] = 1
d["c"] = 2

print(d["a"])
print(d["b"])
print(d["c"])
#%%

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s or len(s) < len(t):
            return ""
        tFreq = collections.defaultdict(int)
        winFreq = collections.defaultdict(int)
        for c in t:
            tFreq[c] += 1
        left, right = 0, 0
        # 滑动窗口内部包含T字符的个数
        distance = 0
        min_len = len(s) + 1
        anscoordinate = [0, 0]
        
        while right < len(s):
            # 当前字符(窗口右侧)频数 < 目标内当前字符频数
            # 右边界向右移动
            if winFreq[s[right]] < tFreq[s[right]]:
                distance += 1
            winFreq[s[right]] += 1
            right += 1

            # 当窗口内包含了所有T字符
            while distance == len(t):
                # 当前字符(窗口左侧)频数 > 目标内当前字符频数
                # 左边界向右移动 left += 1
                if winFreq[s[left]] > tFreq[s[left]]:
                    winFreq[s[left]] -= 1
                    left += 1
                # 当前字符(窗口左侧)频数 <= 目标内当前字符频数 （说明该字符是必要的
                # 减去该字符在窗口字符频率中的频率 -1
                # 减去目标值计数器 distance -=1
                # 左边界向右移动 left += 1
                else:
                    # 如果当前窗口最小，设置当前窗口为最小窗口并记录坐标
                    if right - left < min_len:
                        min_len = right - left
                        anscoordinate = [left, right]
                    winFreq[s[left]] -= 1
                    left += 1
                    distance -= 1
        # 处理S不包含T的情况
        if min_len == len(s) + 1:
            return ""
        # 返回S[ans[0]:ans[1]]
        else:
            return s[anscoordinate[0] : anscoordinate[1]]

