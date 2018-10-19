'''
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
题意：输出满足条件的路径数量，不一定要从根节点到叶节点，但需要是从上往下的顺序
思路：每一个点为开头，做遍历 时间复杂度最差O(n^2)，如果树平衡，就是nlgn
优化：用哈希表记忆路径,curSum是根节点到当前节点的和，oldSum是root到当前节点的父节点的和，如果target存在，
那么必然有oldSum=curSum-target，因此记住oldSum的值，当移动到另一分支时候需要将curSum减1
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def pathSum(self,root,sum):
        # root搜索，root.left开始搜索，root.right开始搜索
        if root:
            return self.findpath(root,sum) + self.pathSum(root.left,sum) + self.pathSum(root.right,sum)
        return 0

    def findpath(self,root,target):
        if root:
            return int(root.val==target) + self.findpath(root.left,target-root.val) + self.findpath(root.right,target-root.val)
        return 0

class Solution2:
    def pathSum(self,root,sum):
        self.res=0
        self.dfs(root,sum,0,{0:1})
        return self.res

    def dfs(self,root,target,curSum,cache):
        # 终止条件
        if not root:
            return
        curSum += root.val
        oldSum = curSum-target
        # 更新res和cache
        self.res+=cache.get(oldSum,0)
        cache[curSum]=cache.get(curSum,0)+1
        # dfs搜索
        self.dfs(root.left,target,curSum,cache)
        self.dfs(root.right, target, curSum, cache)
        # 当移动到不同的分支时候，curSum就无效了，需要去掉
        cache[curSum] -= 1

root=TreeNode(1)
b=TreeNode(3)
root.left=b
c=TreeNode(2)
b.left=c
solution=Solution2()
print(solution.pathSum(root,5))