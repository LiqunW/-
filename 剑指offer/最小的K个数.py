'''
输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。
思路：用最大堆保存K个数，每次只和堆顶比（堆顶存储的是堆的最大值），如果比堆顶小，删掉堆顶，新数入堆，重新调整堆
时间复杂度O(nlogk)
冒泡O(n*k)
利用快排的思想，找出前k个最下的数
'''
# 堆方法，实现插入和删除操作即可
import heapq
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if not tinput or len(tinput)<k or k==0:
            return []
        self.array=[]
        for i in range(k):
            self.heappush(tinput[i])
        for i in range(k,len(tinput)):
            if tinput[i]<self.array[0]:
                self.heappop()
                self.heappush(tinput[i])
        return sorted(self.array)

    def heappush(self,num):
        self.array.append(num)
        length=len(self.array)
        idx=length-1
        while idx>0:
            if self.array[idx]>self.array[(idx-1)//2]:
                self.array[idx],self.array[(idx-1)//2]= \
                self.array[(idx - 1) // 2],self.array[idx]
                idx=(idx-1)//2
            else:
                break
    def heappop(self):
        res=self.array[0]
        self.array[0]=self.array[-1]
        self.array.pop()
        idx=0
        length=len(self.array)
        while idx*2+1<length:
            child=idx*2+1
            if child+1<length and self.array[child]<self.array[child+1]:
                child+=1
            if self.array[idx]<self.array[child]:
                self.array[idx],self.array[child]= \
                self.array[child],self.array[idx]
                idx=child
            else:
                break
        return res


#快排方法
class Solution2:
    def partition(self, arr, startIndex, endIndex):
        i = startIndex - 1
        for j in range(startIndex, endIndex):
            if arr[j] <= arr[endIndex]:
                i += 1
                arr[j], arr[i] = arr[i], arr[j]
        arr[i + 1], arr[endIndex] = arr[endIndex], arr[i + 1]
        return i

    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if k == 0 or not tinput or k > len(tinput):
            return []
        if k == len(tinput):
            return sorted(tinput)
        startIndex = 0
        endIndex = len(tinput) - 1
        index = self.partition(tinput, startIndex, endIndex)
        while index != k - 1:
            if index > k - 1:
                endIndex -= 1
                index = self.partition(tinput, startIndex, endIndex)
            else:
                startIndex += 1
                index = self.partition(tinput, startIndex, endIndex)
        return sorted(tinput[:index + 1])

a=Solution()
print(a.GetLeastNumbers_Solution([4,5,1,6,2,7,3,8],4))