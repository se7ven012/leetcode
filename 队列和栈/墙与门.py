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

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """

        # 无脑暴力解法
        # 以0为中心，向外围计算步数
        # 包含大量重复计算
        if not rooms or len(rooms) == 0:
            return

        col = len(rooms[0])
        row = len(rooms)

        def bsf(rooms, i, j, val):
            nonlocal row, col
            
            #撞墙或超出边框，无效
            if i<0 or i>=row or j<0 or j>=col:
                return
            #有更小的步数了，不需要继续算
            if rooms[i][j]<val:
                return

            rooms[i][j]=val

            #递归调用
            bsf(rooms,i+1,j,val+1) #→
            bsf(rooms,i,j+1,val+1) #↑
            bsf(rooms,i-1,j,val+1) #←
            bsf(rooms,i,j-1,val+1) #↓
        
        #用门坐标开始递归
        for i in range(row):
            for j in range(col):
                if rooms[i][j]==0:
                    bsf(rooms,i,j,0)

            



        