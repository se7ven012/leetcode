# 你被给定一个 m × n 的二维网格，网格中有以下三种可能的初始化值：

#     -1 表示墙或是障碍物
#     0 表示一扇门
#     INF 无限表示一个空的房间。然后，我们用 231 - 1 = 2147483647 代表 INF。你可以认为通往门的距离总是小于 2147483647 的。

# 你要给每个空房间位上填上该房间到 最近 门的距离，如果无法到达门，则填 INF 即可。

# 示例：

# 给定二维网格：

# INF  -1  0  INF
# INF INF INF  -1
# INF  -1 INF  -1
#   0  -1 INF INF

# 运行完你的函数后，该网格应该变成：

#   3  -1   0   1
#   2   2   1  -1
#   1  -1   2  -1
#   0  -1   3   4

# BFS广度优先搜索
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        # # 解法1：
        # # 无脑暴力解法
        # # 以0为中心，向外围计算步数
        # # 包含大量重复计算
        # if not rooms or len(rooms) == 0:
        #     return

        # col = len(rooms[0])
        # row = len(rooms)

        # def bsf(rooms, i, j, val):
        #     nonlocal row, col

        #     #撞墙或超出边框，无效
        #     if i<0 or i>=row or j<0 or j>=col:
        #         return
        #     #有更小的步数了，不需要继续算
        #     if rooms[i][j]<val:
        #         return

        #     rooms[i][j]=val

        #     #递归调用
        #     bsf(rooms,i+1,j,val+1) #→
        #     bsf(rooms,i,j+1,val+1) #↑
        #     bsf(rooms,i-1,j,val+1) #←
        #     bsf(rooms,i,j-1,val+1) #↓

        # #用门坐标开始递归
        # for i in range(row):
        #     for j in range(col):
        #         if rooms[i][j]==0:
        #             bsf(rooms,i,j,0)

        # --------------------------------------------
        # 解法2：
        # 这样写能跑快点
        if not rooms or len(rooms) == 0:
            return

        col, row = len(rooms[0]), len(rooms)

        map = []

        # 先记录门坐标
        for i in range(row):
            for j in range(col):
                if rooms[i][j] == 0:
                    map.append((i, j))

        val = 0

        # 用门坐标算距离

        # 因为while里在对a进行重复赋值，所以一定要等tem为空时while才会停下
        while map:
            val += 1
            temp = []
            # 第一次for循环时门坐标都在map里，第一次for循环结束之后map里的
            # 门坐标就都不存在了。
            # 第二次for循环时map里的门坐标被替换成门周围的有效坐标，第二次
            # 循环实际上是在跑所有步数为1的有效坐标
            # 如此类推直到所有有效坐标消失，tem为空，进而a为空，循环停止
            for x, y in map:
                for moveX, moveY in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    # 这里tem为空的条件是坐标的上下左右都不具备有效坐标
                    if (
                        0 <= moveX < row
                        and 0 <= moveY < col
                        and rooms[moveX][moveY] < val
                        and rooms[moveX][moveY] == 2147483647
                    ):
                        rooms[moveX][moveY] = val
                        temp.append((moveX, moveY))
            # 重新赋值map，循环整个map
            map = temp
