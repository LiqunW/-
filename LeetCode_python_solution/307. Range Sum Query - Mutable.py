'''
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.

Example:

Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
Note:

The array is only modifiable by the update function.
You may assume the number of calls to update and sumRange function is distributed evenly.
题意：端点求和问题（L，R）区间，多次查询
思路：BIT或者线段树
'''
# BIT
class NumArray:
    def __init__(self,nums):
        self.n=len(nums)
        self.nums=nums
        self.BIT=[0]*(self.n+1)
        for i in range(self.n):
            k=i+1
            while k<=self.n:
                self.BIT[k]+=nums[i]
                k+=(k&-k)
    # 把第i个位置的数更新为val
    def update(self,i,val):
        diff,self.nums[i]=val-self.nums[i],val
        i+=1
        while i<=self.n:
            self.BIT[i]+=diff
            i+=(i&-i)

    def sumRange(self,i,j):
        res=0;j=j+1
        while j:
            res+=self.BIT[j]
            j-=(j&-j)
        while i:
            res-=self.BIT[i]
            i-=(i&-i)
        return res

# 线段树
class SegmentTree(object):
    def __init__(self,arr,l,r):
        size = r-l+1
        if size ==1:
            self.left=None
            self.right=None
            self.val=arr[l]
            self.l_index=l
            self.r_index=r
        else:
            self.left=SegmentTree(arr,l,r-size//2)
            self.right=SegmentTree(arr,l+(size-size//2),r)
            self.val = self.left.val + self.right.val
            self.l_index=l
            self.r_index=r

    def find_range_sum(self,l,r):
        if self.l_index==l and self.r_index==r:
            return self.val
        if self.left.r_index<r and self.right.l_index>l:
            return self.left.find_range_sum(l,self.left.r_index)+self.right.find_range_sum(self.right.l_index,r)
        elif self.left.r_index<r:
            return self.right.find_range_sum(l,r)
        else:
            return self.left.find_range_sum(l,r)
    def update(self,i,val):
        if self.l_index==i and self.r_index==i:
            self.val=val
            return
        if self.left.l_index <= i <= self.left.r_index:
            self.left.update(i,val)
        else:
            self.right.update(i,val)
        self.val=self.left.val+self.right.val

class NumArray(object):
    def __init__(self,nums):
        if nums is None or len(nums)==0:
            self.tree=None
        else:
            self.tree=SegmentTree(nums,0,len(nums)-1)

    def update(self,i,val):
        if self.tree:
            self.tree.update(i,val)
    def sumRange(self,i,j):
        if self.tree:
            return self.tree.find_range_sum(i,j)
        else:
            return 0

a=NumArray([1,2,3,4,5,6])
print(a.tree.val)