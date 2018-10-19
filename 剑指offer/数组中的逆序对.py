'''
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组,求出这个数组中的逆序对的总数P。
思路：
1.冒泡排序，每个数和后面的数比较，时间复杂度O[n^2]
2.归并排序，合并时，出现前面的数组值array[i]大于后面数组值array[j]时；
则前面数组array[i]~array[mid]都是大于array[j]的，count += mid+1 - i
'''


count = 0
class Solution:
    def InversePairs(self, data):
        global count
        def MergeSort(lists):
            global count
            if len(lists) <= 1:
                return lists
            num = int( len(lists)/2 )
            left = MergeSort(lists[:num])
            right = MergeSort(lists[num:])
            r, l=0, 0
            result=[]
            while l<len(left) and r<len(right):
                if left[l] < right[r]:
                    result.append(left[l])
                    l += 1
                else:
                    result.append(right[r])
                    r += 1
                    count += len(left)-l
            result += right[r:]
            result += left[l:]
            return result
        MergeSort(data)
        return count
a=Solution()
print(a.InversePairs([2,3,1,4,0]))


class Sollution2:
    def __init__(self):
        self.count=0

    def InversePairs(self,data):
        self.Merge_sort(data)
        return self.count

    def Merge_sort(self,data):
        if len(data)<=1:
            return data
        num=int(len(data)/2)
        left=self.Merge_sort(data[:num])
        right=self.Merge_sort(data[num:])
        return self.Merge(left, right)

    def Merge(self,left,right):
        L, R = 0, 0
        res = []
        while L < len(left) and R < len(right):
            if left[L] < right[R]:
                res.append(left[L])
                L += 1
            else:
                res.append(right[R])
                R += 1
                self.count += len(left) - L
        res += right[R:]
        res += left[L:]
        return res
a=Sollution2()
print(a.InversePairs([2,3,1,4,0]))