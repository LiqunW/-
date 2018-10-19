'''
邮局问题
求村庄内建邮局，使得村庄到邮局的距离之和最小
输入
10 5
1 2 3 6 7 9 11 22 44 50
输出
9
设有m个村庄，分别为 V1 V2 V3 … Vm， 要建n个邮局，分别为P1 P2 P3 … Pn
dp的思路w[i][j]是i到j之间建一个邮局的最小距离w[i][i]==0
dp[i][j]是第1个村庄到j个之间建i个邮局的最小距离dp[0][j]表示第一个村庄到第j个村庄间建1个邮局的最小距离
'''
import sys
def minDistance(arr, num):
    if arr==None or len(arr)==0 or num<1 or len(arr)<num:
        return 0
    w=[[0]*(len(arr)+1) for i in range(len(arr)+1)]
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            w[i][j]=w[i][j-1]+arr[j]-arr[(i+j)//2]
    dp=[[0]*len(arr) for i in range(num)]
    for j in range(1,len(arr)):
        dp[0][j]=w[0][j]

    for i in range(1,num):
        for j in range(i+1,len(arr)):
            dp[i][j]=sys.maxsize
            for k in range(j+1):
                dp[i][j]=min(dp[i][j],dp[i-1][k]+w[k+1][j])
    return dp[num-1][len(arr)-1]


print(minDistance([1,2,3,6,7,9,11,22,44,50],5))



