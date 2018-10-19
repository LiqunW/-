'''
关于“恰好装满”
如果要求恰好装满背包，可以在初始化时除 dp[0] 或 dp[i][0] 初始化 0，其他初始化为 -INF。这样即可保证最终得到的 dp[N] 或 dp[N][M] 是一种恰好装满背包的解；
如果不要求恰好装满，则全部初始化为 0 即可。
可以这样理解：初始化的 dp 数组实际上就是在没有任何物品可以放入背包时的合法状态。
如果要求背包恰好装满，那么此时只有容量为 0 的背包可能被价值为 0 的物品“恰好装满”，其它容量的背包均没有合法的解，属于未定义的状态，它们的值就都应该是 -INF 。
如果背包并非必须被装满，那么任何容量的背包都有一个合法解，即“什么都不装”，这个解的价值为0，所以初始时状态的值也全部为 0 。

实际实现时候，从后往前遍历dp数组，如果dp[-1]的值出现了不止一次，说明背包没有装满（dp[-1]是背包装满的情况下获得的最大值）
'''

'''
背包问题一（最大放入重量），选或者不选
背包11，物品[2,3,5,7]
输出 10
dp解决
状态转移方程dp[j]=max(dp[j],dp[j-A[i]]+A[i])
'''
def bagpack1(bag_limit,nums):
    dp=[0]*(bag_limit+1)
    for i in range(len(nums)):
        for j in range(bag_limit,0,-1):
            if j>=nums[i]:
                dp[j]=max(dp[j],dp[j-nums[i]]+nums[i])
    return dp[bag_limit]

maxweight=12
nums=[2,3,5,7]
print(bagpack1(maxweight,nums))

# 输出最优解 dfs 所有的可能性（组合（不考虑顺序））
class Solution:
    def bagpack(self,limit,nums):
        nums.sort(reverse=True)
        self.res=[]
        self.dfs(nums,limit,[])
        return self.res

    def dfs(self,nums,target,path):
        if target<0:
            return
        elif target==0:
            self.res.append(path)
            return
        for i in range(len(nums)):
            if path and path[-1]>nums[i] or path==[]:
                self.dfs(nums[:i]+nums[i+1:],target-nums[i],path+[nums[i]])
        return
so=Solution()
maxweight=12
nums=[2,3,5,7]
print(so.bagpack(maxweight,nums))

'''
背包问题二（放入最大价值），选或者不选
背包10
重量W=[2,3,5,7]
价值V=[1,5,2,4]
输出9

dp解决
状态转移方程dp[j]=dp[j-1]+dp[j-W[i]]+V[i]
'''

def bagpack2(limit,weights,values):
    dp=[0]*(limit+1)
    for i in range(len(weights)):
        for j in range(limit,0,-1):
# 从后向前更新 本轮的更新依赖的是上轮更新的值，如果从前向后，那么上轮的值在被使用到之前就被覆盖了
            if j-weights[i]>=0:
                dp[j]=max(dp[j],dp[j-weights[i]]+values[i])
    return dp[limit]

limit=10
w=[2,1,5,7]
v=[4,5,2,4]
print(bagpack2(limit,w,v))
'''输出最优解
用二维dp做方便'''
def bagpack2_1(limit,weight,values):
    dp=[[0]*(limit+1) for _ in range(len(weight)+1)]
    for i in range(len(weight)):
        for j in range(limit+1):
            if j<weight[i]:
                dp[i+1][j]=dp[i][j]
            else:
                dp[i+1][j]=max(dp[i][j],dp[i][j-w[i]]+values[i])
    j=limit
    vis=[0]*(len(weight)+1)
    for i in range(len(weight),0,-1):
        if dp[i][j]>dp[i-1][j]:
            vis[i]=1
            j -= weight[i-1]
        else:
            vis[i]=0
    return dp[-1][-1],vis[1:]
limit = 12
w=[4, 6, 5, 2, 1]
v=[8, 20, 6, 8, 7]
print(bagpack2_1(limit,w,v))


'''
背包问题三（放入最大值），物品无限
背包10
w=[2,3,5,7]
v=[1,5,2,4]
输出15
'''
def bagpack3(limit,weights,values):
    dp=[0]*(limit+1)
    for i in range(len(weights)):
        for j in range(1,limit+1):
            if j-weights[i]>=0:
                dp[j]=max(dp[j],dp[j-weights[i]]+values[i])
    return dp[limit]
limit=10
w=[2,3,5,7]
v=[1,5,2,4]
print(bagpack3(limit,w,v))
