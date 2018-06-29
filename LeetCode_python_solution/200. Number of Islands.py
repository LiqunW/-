'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
题意：岛屿的数量，连成一片的算一个岛屿
思路：dfs，每次搜索完后将当期位置置0，防止重复搜索
'''


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # 异常检查，防止矩阵为空
        if not grid or len(grid[0]) == 0:
            return 0
        count = 0
        # 遍历每个点，从1开始dfs搜索,搜索结束数量+1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.helper(i, j, grid)
                    count += 1
        return count

    def helper(self, i, j, grid):
        steps = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        if i < 0 or j < 0 or i > len(grid) - 1 or j > len(grid[0]) - 1 or grid[i][j] != '1':
            return
        grid[i][j] = '0'
        for nx, ny in steps:
            self.helper(i + nx, j + ny, grid)
