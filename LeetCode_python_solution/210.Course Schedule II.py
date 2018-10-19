'''
题意和207一致，只不过是输出课程选修顺序
思路：拓扑排序，每轮结束后把度为0的点删除之前，把该点加入res中，如果可以排序，输出res，否则输出空
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
            res=[]
            for x in courses:
                if degrees[x]==0: #找到度为0的点，并且删除该点和其他节点相连的边
                    for child in childs[x]:
                        degrees[child]-=1
                    removeList.append(x)
                    flag=True
            for x in removeList:
                res.append(x)
                courses.remove(x)
        return res if len(courses)==0 else []