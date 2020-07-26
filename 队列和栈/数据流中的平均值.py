# Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

# Example:

# MovingAverage m = new MovingAverage(3);
# m.next(1) = 1
# m.next(10) = (1 + 10) / 2
# m.next(3) = (1 + 10 + 3) / 3
# m.next(5) = (10 + 3 + 5) / 3

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
 
class MovingAverage:
    # 跑的慢
    # def __init__(self, size: int):
    #     """
    #     Initialize your data structure here.
    #     """
    #     self.size = size
    #     self.nums = []
    #     self.currSum =0

    # def next(self, val: int) -> float:
    #     self.nums.append(val)
    #     self.currSum = sum(self.nums[-self.size:])
    #     # 直接从两数取最小这样不用写if else
    #     return self.currSum/min(self.size, len(self.nums))
    

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.nums = [0]*size
        self.pointerr = 0
        self.count = 0

    #求和没有顺序要求所以直接用一个指针
    def next(self, val: int) -> float:
        self.nums[self.pointerr]=val
        self.pointerr = (self.pointerr+1) % self.size
        if self.count < self.size:
            self.count += 1
        return sum(self.nums)/self.count


