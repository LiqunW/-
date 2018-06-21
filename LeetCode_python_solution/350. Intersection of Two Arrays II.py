'''
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such
that you cannot load all elements into the memory at once?

题意：找出两个数组中共同元素
思路：
1.先对两个数组排序，然后维持两个指针分别扫描两个数组，找共同元素
2.用字典统计第一个列表都出现了哪些数及出现的次数，然后顺序遍历第二个列表，
发现同时出现的数则加入到结果列表中，同时将第一个列表中相应的出现次数减一。
3.先对第二个列表先排序，每次检查元素是否出现时用二分搜索。
'''

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res=[]
        p1,p2=0,0
        nums1.sort();nums2.sort()
        while p1<len(nums1) and p2<len(nums2):
            if nums1[p1]<nums2[p2]:
                p1+=1
            elif nums1[p1]>nums2[p2]:
                p2+=1
            else:
                res.append(nums1[p1])
                p1+=1
                p2+=1
        return res

class Solution2(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res=[]
        nums2.sort()
        for k in nums1:
            flag,j=self.binarySearch(nums2,k)
            if flag:
                res.append(j)
                del nums2[j]
        return res

    def binarySearch(self,nums,num):
        left=0
        right=len(nums)-1
        while left<=right:
            mid=left+(right-left)//2
            if nums[mid]==num:
                return True,mid
            elif nums[mid]<num:
                left=mid+1
            else:
                right=mid-1
        return False,-1