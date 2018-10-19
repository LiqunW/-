'''
给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。
例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，那么一共存在6个滑动窗口，
他们的最大值分别为{4,4,6,6,6,5}； 针对数组{2,3,4,2,6,2,5,1}的滑动窗口有以下6个：
{[2,3,4],2,6,2,5,1}， {2,[3,4,2],6,2,5,1}， {2,3,[4,2,6],2,5,1}， {2,3,4,[2,6,2],5,1}，
{2,3,4,2,[6,2,5],1}， {2,3,4,2,6,[2,5,1]}。
思路：
(1）判断当前的最大值是否过期。
(2）将读入的数字与 temp 中的元素从后向前依次比较大小，将 temp 中小于读入数字的元素都弹出；
如果删除后 temp 的大小还没有达到 size - 1，那么将这个元素压入（
删除后 temp 的大小有可能达到 size - 1 嘛？有可能的！因为可能经过比较发现 temp 中没有元素被弹出）。
'''

# -*- coding:utf-8 -*-
class Solution:
    def maxInWindows(self, num, size):
        # write code here
        if not num:
            return []
        if size>len(num) or size<1:
            return []
        if size==1:
            return num
        win_max = [0] #存放的是下标
        res=[]
        for i in range(len(num)):
            if i-win_max[0]> size-1: # 队首元素不在当前滑动窗口的范围内，把该元素去掉
                win_max.pop(0)
            while (len(win_max)>0 and num[i]>=num[win_max[-1]]): # 第i个元素和存放的元素比较，去掉比i小的
                win_max.pop()
            if len(win_max)<size: # 如果win_max存放的值没有超过最大规模，就把i放进去
                win_max.append(i)
            if i>=size-1:
                res.append(num[win_max[0]])  # 经历一个完整的窗口了，才把结果加入res中，
        return res

a=Solution()
print(a.maxInWindows([7,6,5,4,3,2,1],3))