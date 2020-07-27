# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

# 岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。

# 此外，你可以假设该网格的四条边均被水包围。


# 示例 1:

# 输入:
# [
# ['1','1','1','1','0'],
# ['1','1','0','1','0'],
# ['1','1','0','0','0'],
# ['0','0','0','0','0']
# ]
# 输出: 1

# 示例 2:

# 输入:
# [
# ['1','1','0','0','0'],
# ['1','1','0','0','0'],
# ['0','0','1','0','0'],
# ['0','0','0','1','1']
# ]
# 输出: 3
# 解释: 每座岛屿只能由水平和/或竖直方向上相邻的陆地连接而成。


# DFS深度优先搜索
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        row = len(grid)
        if row ==0:
            return 0
        col = len(grid[0])
        islands = 0

        def dfs(grid, i, j):
            nonlocal col, row
            # 设置该点已遍历
            grid[i][j] = 0
            for moveX, moveY in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= moveX < row and 0 <= moveY < col and grid[moveX][moveY] == "1":
                    dfs(grid, moveX, moveY)

        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    islands += 1
                    dfs(grid, i, j)

        return islands

