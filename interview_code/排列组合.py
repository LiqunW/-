'''
全排列
[5,4,3],输出的是全排列，也可以是抽取n个数的全排列
[[5, 4], [5, 3], [4, 5], [4, 3], [3, 5], [3, 4]]
'''


class Solution:
    def __init__(self):
        self.res=[]

    def permu(self,nums):
        picknum=2
        self.dfs([],nums,picknum)
        return self.res

    def dfs(self,path,nums,lens):
        if lens==0:
            self.res.append(path)
            return
        for i in range(len(nums)):
            self.dfs(path+[nums[i]],nums[:i]+nums[i+1:],lens-1)
a=Solution()
print(a.permu([5,4,3]))


'''
组合[5,4,3,2,1]，抽n个数的组合
'''
class Solution2:
    def __init__(self):
        self.res=[]

    def comb(self,nums):
        self.dfs([],nums,2,0)
        return self.res

    def dfs(self,path,nums,lens,start):
        if lens==0:
            self.res.append(path)
            return
        for i in range(start,len(nums)):
            self.dfs(path+[nums[i]],nums,lens-1,i+1)

a=Solution2()
print(a.comb([5,4,3,2,1]))

'''
组合[5,4,3,2,1]，抽所有可能的组合
1个数的组合，2个。。。。5个
'''
class Solution3:
    def __init__(self):
        self.res=[]

    def comb_all(self,nums):
        for i in range(1,len(nums)+1):
            self.dfs([],nums,i,0)
        return self.res

    def dfs(self,path,nums,lens,start):
        if lens==0:
            self.res.append(path)
            return
        for i in range(start,len(nums)):
            self.dfs(path+[nums[i]],nums,lens-1,i+1)

a=Solution3()
print(a.comb_all([5,4,3,2,1]))