# 设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。

#     push(x) —— 将元素 x 推入栈中。
#     pop() —— 删除栈顶的元素。
#     top() —— 获取栈顶元素。
#     getMin() —— 检索栈中的最小元素。

# 示例:

# 输入：
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]

# 输出：
# [null,null,null,null,-3,null,0,-2]

# 解释：
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> 返回 -3.
# minStack.pop();
# minStack.top();      --> 返回 0.
# minStack.getMin();   --> 返回 -2.

# 提示：pop、top 和 getMin 操作总是在 非空栈 上调用。

class MinStack(object):
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data=[]
        self.helper=[]


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.data.append(x)
        # 这里“等于”要考虑进去，因为出栈的时候，连续的、相等的并且是最小值的元素要同步出栈；
        if len(self.helper)==0 or x<=self.helper[-1]:
            self.helper.append(x)


    def pop(self):
        """
        :rtype: None
        """
        # 数据栈先取
        top = self.data.pop()
        # 看看辅助栈的值和数据栈是否一样，若一样就删除顶端的值
        if self.helper and top ==self.helper[-1]:
            self.helper.pop()
        return top


    def top(self):
        """
        :rtype: int
        """
        # 返回数据栈的栈顶元素
        if self.data:
            return self.data[-1]


    def getMin(self):
        """
        :rtype: int
        """
        # 返回辅助栈的栈顶元素
        if self.data:
            return self.helper[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()