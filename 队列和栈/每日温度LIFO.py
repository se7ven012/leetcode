# 请根据每日 气温 列表，重新生成一个列表。对应位置的输出为：要想观测到更高的气温，至少需要等待的天数。如果气温在这之后都不会升高，请在该位置用 0 来代替。

# 例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。

# 提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。

# 单调栈
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        length = len(T)
        anw = [0] * length
        # 该栈只存索引
        stack = []

        for i in range(length):
            temperature = T[i]
            # 如果当前温度比栈里最后一位温度高的话
            # 就能用当前温度索引减去栈里最后一位温度
            # 的索引从而给栈里最后一位温度的索引赋值
            while stack and temperature > T[stack[-1]]:
                prev_index = stack.pop()
                anw[prev_index] = i - prev_index
            # 如果栈是空的 或当前索引温度比栈里最后一位温度小
            # 就直接把当前索引压入栈
            stack.append(i)
        return anw