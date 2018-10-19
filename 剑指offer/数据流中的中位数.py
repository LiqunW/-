# -*- coding:utf-8 -*-
'''
如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。
如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。
我们使用Insert()方法读取数据流，使用GetMedian()方法获取当前读取数据的中位数。
维护一个大顶堆和一个小顶堆，奇数个数插入到大堆中，偶数个数插入到小堆中

注意不是直接进入小根堆，而是经大根堆筛选后取大根堆中最大元素进入小根堆）
当数据总数为奇数时，新加入的元素，应当进入大根堆
注意不是直接进入大根堆，而是经小根堆筛选后取小根堆中最大元素进入大根堆）
'''

class Solution:
    def __init__(self):
        self.minNums=[]
        self.maxNums=[]
    def maxHeapInsert(self,num): #堆中进入一个元素后，进行堆的调整
        self.maxNums.append(num)
        lens = len(self.maxNums)
        i = lens - 1
        while i > 0:
            if self.maxNums[i] > self.maxNums[(i - 1) // 2]:
                t = self.maxNums[(i - 1) // 2]
                self.maxNums[(i - 1) // 2] = self.maxNums[i]
                self.maxNums[i] = t
                i = (i - 1) // 2
            else:
                break

    def maxHeapPop(self): # 弹出一个元素后，堆调整
        t = self.maxNums[0]
        self.maxNums[0] = self.maxNums[-1]
        self.maxNums.pop()
        lens = len(self.maxNums)
        i = 0
        while 2 * i + 1 < lens:
            nexti = 2 * i + 1
            if (nexti + 1 < lens) and self.maxNums[nexti + 1] > self.maxNums[nexti]:
                nexti += 1
            if self.maxNums[nexti] > self.maxNums[i]:
                tmp = self.maxNums[i]
                self.maxNums[i] = self.maxNums[nexti]
                self.maxNums[nexti] = tmp
                i = nexti
            else:
                break
        return t

    def minHeapInsert(self,num):
        self.minNums.append(num)
        lens = len(self.minNums)
        i = lens - 1
        while i > 0:
            if self.minNums[i] < self.minNums[(i - 1) / 2]:
                t = self.minNums[(i - 1) / 2]
                self.minNums[(i - 1) / 2] = self.minNums[i]
                self.minNums[i] = t
                i = (i - 1) / 2
            else:
                break

    def minHeapPop(self):
        t = self.minNums[0]
        self.minNums[0] = self.minNums[-1]
        self.minNums.pop()
        lens = len(self.minNums)
        i = 0
        while 2 * i + 1 < lens:
            nexti = 2 * i + 1
            if (nexti + 1 < lens) and self.minNums[nexti + 1] < self.minNums[nexti]:
                nexti += 1
            if self.minNums[nexti] < self.minNums[i]:
                tmp = self.minNums[i]
                self.minNums[i] = self.minNums[nexti]
                self.minNums[nexti] = tmp
                i = nexti
            else:
                break
        return t

    def Insert(self, num):
        # 始终保证了大根堆的堆顶小于小根堆的堆顶(大堆是数据流前半部分，小堆是数据流后半部分)
        if (len(self.minNums)+len(self.maxNums))&1==0:
            # 偶数个元素时候入小堆，先经过大堆筛选，选出大堆的最大值
            if len(self.maxNums)>0 and num < self.maxNums[0]:
                self.maxHeapInsert(num)
                num = self.maxHeapPop()
            self.minHeapInsert(num)
        else:
            # 奇数个元素时候入大堆，先经过小堆筛选，选出最小值
            if len(self.minNums)>0 and num > self.minNums[0]:
                self.minHeapInsert(num)
                num = self.minHeapPop()
            self.maxHeapInsert(num)

    def GetMedian(self,n=None):
        allLen = len(self.minNums) + len(self.maxNums)
        if allLen ==0:
            return -1
        if allLen &1==1:  # 奇数就返回小根堆中的堆首元素
            return self.minNums[0]
        else: # 偶数返回堆首均值
            return (self.maxNums[0] + self.minNums[0]+0.0)/2
# heapq实现的是小根堆，要想完成大根堆的功能，可以将一个数的相反数存入堆中，弹出的时候返回相反数即可
import heapq
class Solution2:
    def __init__(self):
        self.minNums=[]
        self.maxNums=[]
    def Insert(self, num):
        if (len(self.minNums) + len(self.maxNums)) & 1 == 0:
            if len(self.maxNums) > 0 and num < -self.maxNums[0]:
                heapq.heappush(self.maxNums,-num) #进入大根堆
                num = -heapq.heappop(self.maxNums)
            heapq.heappush(self.minNums,num)
        else:
            if len(self.minNums)>0 and num>self.minNums[0]:
                heapq.heappush(self.minNums,num)
                num = heapq.heappop(self.minNums)
            heapq.heappush(self.maxNums,-num)

    def GetMedian(self, n=None):
        lens = len(self.minNums) + len(self.maxNums)
        if lens==0:
            return -1
        if lens &1==1:  # 奇数就返回小根堆中的堆首元素
            return self.minNums[0]
        else: # 偶数返回堆首均值
            return (-self.maxNums[0] + self.minNums[0]+0.0)/2