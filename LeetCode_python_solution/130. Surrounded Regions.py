'''
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'.
Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'.
Two cells are connected if they are adjacent cells connected horizontally or vertically.

题意：把所有被包围的O替换成X，O不能在边上

思路：从边上开始搜索，如果是'O'，那么搜索'O'周围的元素，并将'O'置换为'D'，这样每条边都DFS或者BFS一遍。
而内部的'O'是不会改变的。这样下来，没有被围住的'O'全都被置换成了'D'，被围住的'O'还是'O'，没有改变。然后遍历一遍，将'O'置换为'X'，将'D'置换为'O'。
'''
# dfs解法
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(board) == 0: return
        row = len(board);col = len(board[0])
        # 从边上的每一个点开始搜索
        for i in range(row):
            self.dfs(board, i, 0, row, col)
            self.dfs(board, i, col - 1, row, col)
        for i in range(1, col - 1):
            self.dfs(board, 0, i, row, col)
            self.dfs(board, col - 1, i, row, col)

        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'D':
                    board[i][j] = 'O'

    def dfs(self, board, x, y, row, col):
        if x < 0 or x > row - 1 or y < 0 or y > col - 1 or board[x][y] != 'O':
            return
        board[x][y] = 'D'
        self.dfs(board, x - 1, y, row, col)
        self.dfs(board, x + 1, y, row, col)
        self.dfs(board, x, y + 1, row, col)
        self.dfs(board, x, y - 1, row, col)

# bfs 解法 注意queue的用法，只有满足情况的条件下才改变这个值
class Solution2(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def fill(x, y):
            if x<0 or x>m-1 or y<0 or y>n-1 or board[x][y] != 'O': return
            queue.append((x,y))
            board[x][y]='D'

        def bfs(x, y):
            if board[x][y]=='O':
                queue.append((x,y)); fill(x,y)
            while queue:
                curr=queue.pop(0); i=curr[0]; j=curr[1]
                fill(i+1,j);fill(i-1,j);fill(i,j+1);fill(i,j-1)

        if len(board)==0: return
        m=len(board); n=len(board[0]); queue=[]
        for i in range(n):
            bfs(0,i); bfs(m-1,i)
        for j in range(1, m-1):
            bfs(j,0); bfs(j,n-1)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'D': board[i][j] = 'O'
                elif board[i][j] == 'O': board[i][j] = 'X'