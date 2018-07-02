'''
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
思路：二分查找的思路，找到的最小值恰好能够分割这两个数组
用low指针指向数组开头，high指针指向数组尾部，当low指针和high指针只差一位时，判断结束
mid=(low+high)/2，如果array[mid]>=array[low],说明最小值在后半部分，如果array[mid]<=array[low]
说明在前半部分，对于三个数都相等的情况，顺序查找
'''
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray) == 0:
            return 0
        low = 0
        high = len(rotateArray)-1
        minVal = rotateArray[low]
        while high - low > 1:
            middle = (low+high)//2
            if rotateArray[low] <= rotateArray[middle]:
                    low = middle
            elif rotateArray[low]>=rotateArray[middle]:
                    high = middle
            elif rotateArray[middle] == rotateArray[low] and rotateArray[low] == rotateArray[high]:
                    for i in range(low, high+1):
                        if rotateArray[i] < minVal:
                            minVal = rotateArray[i]
                            high= i
        minVal = rotateArray[high]
        return minVal