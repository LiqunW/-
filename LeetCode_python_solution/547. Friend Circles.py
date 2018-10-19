'''
There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend circles among all the students.

Example 1:
Input:
[[1,1,0],
 [1,1,0],
 [0,0,1]]
Output: 2
Explanation:The 0th and 1st students are direct friends, so they are in a friend circle.
The 2nd student himself is in a friend circle. So return 2.
Example 2:
Input:
[[1,1,0],
 [1,1,1],
 [0,1,1]]
Output: 1
Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends,
so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.
Note:
N is in range [1,200].
M[i][i] = 1 for all students.
If M[i][j] = 1, then M[j][i] = 1.
题意：朋友圈，A和B互为朋友，则形成一个朋友圈，B和C互为朋友，也是一个朋友圈，ABC合并成同一个朋友圈。
思路：1.并查集
遍历矩阵M，如果M[x][y]==1，合并(x,y)
统计未被合并（祖先等于其本身）的节点个数即为答案
2.DFS/BFS
'''
# 并查集
class Solution:
    def findCircleNum(self,M):
        N=len(M)
        fc=list(range(N))

        def find(x): #路径缩短方法，指向组的根节点
            while fc[x] != x:
                x=fc[x]
            return x
        for x in range(N):
            for y in range(x+1,N):
                if M[x][y]:
                    fc[find(x)]=find(y) #把属于同一个朋友圈的人合并
        return sum(fc[x]==x for x in range(N))

class Solution2:
    def findCircleNum(self,M):
        N=len(M);cnt=0
        self.visited=set()
        for i in range(N):
            if i not in self.visited:
                cnt+=1 # 一个人也能形成朋友圈，所以先+1
                self.dfs(i,N,M) # 搜索朋友圈里有哪几个人
        return cnt

    def dfs(self,i,N,M):
        for x in range(N):
            if M[i][x] and x not in self.visited: # 第i个人和第x个人是朋友，且x还没有访问过
                self.visited.add(x)
                self.dfs(x,N,M)