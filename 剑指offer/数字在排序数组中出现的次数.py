'''
数字在排序数组中出现的次数
二分查找，当头，尾，中间值等于目标时，像两边搜索
'''

class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        if not data:
            return 0
        L=0;R=len(data)-1
        cnt=0
        while L<=R:
            mid=(R-L)//2+L
            if data[L]==k:
                while L<=len(data)-1 and data[L]==k:
                    cnt+=1
                    L+=1
                return cnt
            elif data[R]==k:
                while R>=0 and data[R]==k:
                    cnt+=1
                    R-=1
                return cnt
            elif data[mid]==k and data[L]!=k and data[R]!=k:
                st=mid;end=mid+1
                while st>=0 and data[st]==k:
                    cnt+=1
                    st-=1
                while end<=len(data)-1 and data[end]==k:
                    cnt+=1
                    end+=1
                return cnt
            if data[mid]<k:
                L=mid+1
            if data[mid]>k:
                R=mid-1
        return cnt

a=Solution()
print(a.GetNumberOfK([3,3,3,3,3],3))