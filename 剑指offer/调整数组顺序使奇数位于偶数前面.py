'''
题意：输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，
所有的偶数位于位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
思路：
'''
class Solution:
    def reOrderArray(self, array):
        # write code here
        evencnt=0
        lens=len(array)-1
        idx=0
        while idx<=lens-evencnt:
            if array[idx]%2==0:
                tmp=array[idx]
                del array[idx]
                evencnt+=1
                array.append(tmp)
            else:
                idx+=1
        return array
a=Solution()
print(a.reOrderArray([1,2,3,4,5]))