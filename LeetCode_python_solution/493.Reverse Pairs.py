'''
Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].

You need to return the number of important reverse pairs in the given array.

Example1:

Input: [1,3,2,3,1]
Output: 2
Example2:

Input: [2,4,3,5,1]
Output: 3
Note:
The length of the given array will not exceed 50,000.
All the numbers in the input array are in the range of 32-bit integer.
题意：找到逆序对（两倍大小）
思路：1.BST
2.BIT（Binary Indexed Tree树状数组）
3.Merge Sort
'''


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.count_ge = 1

# BST做法
class Solution:
    def insert(self,head,val):
        if head is None:
            return Node(val)
        elif val==head.val:
            head.count_ge+=1
        elif val<head.val:
            head.left=self.insert(head.left,val)
        else:
            head.count_ge+=1
            head.right = self.insert(head.right, val)

    def search(self,head,target):
        if head is None:
            return 0
        elif target == head.val:
            return head.count_ge
        elif target < head.val:
            return head.count_ge + self.search(head.left, target)
        else:
            return self.search(head.right, target)

    def reversePairs(self,nums):
        head=Node(nums[0])
        count=0
        for num in nums[1:]:
            count += self.search(head,num*2+1)
            self.insert(head,num)
        return count

so=Solution()
nums=[3,5,2,1,3,1,2]
print(so.reversePairs(nums))


# BIT做法
class BIT:
    def __init__(self,n):
        self.n=n+1
        self.sums=[0]*self.n

    def update(self, i, delta):
        while i < self.n:
            self.sums[i] += delta
            i += i & (-i)

    def query(self, i):
        res=0
        while i > 0:
            res += self.sums[i]
            i -= i & (-i)
        return res


class Solution2:
    def reversePairs(self, nums):
        new_nums = nums + [x*2 for x in nums]
        sorted_set = sorted(list(set(new_nums)))
        tree = BIT(len(sorted_set))
        res = 0
        ranks = {}
        for i, n in enumerate(sorted_set):
            ranks[n] = i+1
        for n in nums[::-1]:
            res += tree.query(ranks[n]-1)
            tree.update(ranks[n*2], 1)
        return res
so=Solution2()
nums=[3,5,2,1,3,1,2]
print(so.reversePairs(nums))

# 归并排序做法
class Solution3:
    def reversePairs(self, nums):
        def merge(nums,start,mid,end): # 归并排序过程，小的数字放在前面
            r=mid+1
            tmp=[]
            for i in range(start,mid+1):
                while r <= end and nums[i] > nums[r]:
                    tmp.append(nums[r])
                    r += 1
                tmp.append(nums[i])
            nums[start:start+len(tmp)] = tmp

        def countAndMergeSort(nums,start,end):
            if end - start <= 0:
                return 0
            mid = start + (end - start) // 2
            count = countAndMergeSort(nums,start,mid)+countAndMergeSort(nums,mid+1,end)
            r = mid + 1
            for i in range(start, mid+1):
                while r <= end and nums[i] > nums[r] * 2:
                    r +=1
                count += r - (mid+1)
            merge(nums, start, mid, end)
            return count
        return countAndMergeSort(nums, 0, len(nums)-1)

so=Solution3()
nums=[3,5,2,1,3,1,2]
print(so.reversePairs(nums))