'''
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.
题意：硬币找零问题（可重复使用硬币）
思路：dp的思路，dp[i+j]=min(dp[i+j],dp[i]+1)，j是硬币面值
bfs，从0出发到目标，每一步可走的距离是硬币面值
对于硬币不能重复的情况，用dfs更好些
'''
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp=[0]+[-1]*amount
        for i in range(amount):
            if dp[i]<0:
                continue
            for j in coins:
                if i+j>amount:
                    continue
                if dp[i+j]<0 or dp[i+j]>dp[i]+1:
                    dp[i+j]=dp[i]+1
        return dp[amount]

class Solution2(object):
    def coinChange(self,coins,amount):
        if amount==0:
            return 0
        value=[0]
        value_next=[]
        nc=0
        visited=[False]*(amount+1)
        visited[0]=True
        while value:
            nc+=1
            for v in value:
                for coin in coins:
                    newval=v+coin
                    if newval==amount:
                        return nc
                    elif newval>amount:
                        continue
                    elif not visited[newval]:
                        visited[newval]=True
                        value_next.append(newval)
            value,value_next=value_next,[]
        return -1

#硬币不能重复使用的情况
class Solution_(object):
    def make_change(self,coins,amount):
        if amount==0:
            return 0
        self.steps=len(coins)+1
        self.dfs(coins,amount,0,0,len(coins))
        return self.steps if self.steps<len(coins)+1 else -1
    def dfs(self,coins,amount,value,step,length):
        if value==amount :
            self.steps=min(self.steps,step)
            return
        elif value> amount or step>length:
            return
        else:
            for i in range(len(coins)):
                self.dfs(coins[:i]+coins[i+1:],amount,value+coins[i],step+1,length)

a=Solution_()
print(a.make_change([1],0))

