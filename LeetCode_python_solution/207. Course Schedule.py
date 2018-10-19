'''
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1,
which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:

Input: 2, [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
Note:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices.
Read more about how a graph is represented.You may assume that there are no duplicate edges in the input prerequisites.

题意：给定一些课程，以及课程之间的先修关系，问是否可能完成这些课程。
思路：拓扑排序（Topological Sort） 参考 https://www.hrwhisper.me/leetcode-graph/
1. 每次找入度为0的点，输出该入度为0的点，并删除与之相连接的边
2. 重复1直到没有入度为0的点。之前输出入度为0的点若小于原图的结点数，那么说明图有环，即拓扑排序不存在，否则即为拓扑排序。
'''

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        degrees = [0]*numCourses #每个节点的度
        childs=[[] for x in range(numCourses)] #边
        for pair in prerequisites:
            degrees[pair[0]]+=1 #依赖课程的度+1
            childs[pair[1]].append(pair[0]) # 依赖课程和后修课程连接
        courses=set(range(numCourses))
        flag=True
        while flag and len(courses): #遍历课程，直到所有课程都删除或者不存在度为0的点
            flag=False
            removeList=[]
            for x in courses:
                if degrees[x]==0: #找到度为0的点，并且删除该点和其他节点相连的边
                    for child in childs[x]:
                        degrees[child]-=1
                    removeList.append(x)
                    flag=True
            for x in removeList:
                courses.remove(x)
        return len(courses)==0