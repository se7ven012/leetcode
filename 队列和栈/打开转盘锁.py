# 你有一个带有四个圆形拨轮的转盘锁。每个拨轮都有10个数字： '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' 。每个拨轮可以自由旋转：例如把 '9' 变为  '0'，'0' 变为 '9' 。每次旋转都只能旋转一个拨轮的一位数字。

# 锁的初始数字为 '0000' ，一个代表四个拨轮的数字的字符串。

# 列表 deadends 包含了一组死亡数字，一旦拨轮的数字和列表里的任何一个元素相同，这个锁将会被永久锁定，无法再被旋转。

# 字符串 target 代表可以解锁的数字，你需要给出最小的旋转次数，如果无论如何不能解锁，返回 -1。


# 示例 1:

# 输入：deadends = ["0201","0101","0102","1212","2002"], target = "0202"
# 输出：6
# 解释：
# 可能的移动序列为 "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202"。
# 注意 "0000" -> "0001" -> "0002" -> "0102" -> "0202" 这样的序列是不能解锁的，
# 因为当拨动到 "0102" 时这个锁就会被锁定。

# 示例 2:

# 输入: deadends = ["8888"], target = "0009"
# 输出：1
# 解释：
# 把最后一位反向旋转一次即可 "0000" -> "0009"。

# 示例 3:

# 输入: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
# 输出：-1
# 解释：
# 无法旋转到目标数字且不被锁定。

# 示例 4:

# 输入: deadends = ["0000"], target = "8888"
# 输出：-1


# BFS
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # 从0000开始找，每个8种可能性
        def bfs(node):
            # 迭代每位锁
            for i in range(4):
                # 上下拨动锁
                x = int(node[i])
                for move in (-1, 1):
                    y = (x + move) % 10
                    yield node[:i] + str(y) + node[i + 1 :]

        dead = set(deadends)
        queue = collections.deque([("0000", 0)])
        seen = {"0000"}

        # queue是自循环用的
        while queue:
            # queue保存所有尝试过的解
            node, depth = queue.popleft()
            if node == target:
                return depth
            # 当前node在dead里也没关系，换下一个node跑
            if node in dead:
                continue
            # 递归调用bfs
            for tri in bfs(node):
                # bfs会试完当前node的8种解
                if tri not in seen:
                    seen.add(tri)
                    # 把没见过的node加入自循环
                    queue.append((tri, depth + 1))
        return -1
