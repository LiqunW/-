'''
在一个长度为n的数组里的所有数字都在0到n-1的范围内。 数组中某些数字是重复的，但不知道有几个数字是重复的。也不知道每个数字重复几次。
请找出数组中任意一个重复的数字。 例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2。
思路1：哈希
思路2：因为所有的数都是在0-n-1的范围里，所以当一个数字被访问过后，可以设置对应位置上的数 + n，之后再遇到相同的数时，
会发现对应位置上的数已经大于等于n了，那么直接返回这个数即可
'''

import collections
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        num_dict=collections.defaultdict(int)
        for i in numbers:
            num_dict[i]+=1
            if num_dict[i]==2:
                duplication[0]=i
                return True
        return False

class Solution2:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        length=len(numbers)
        for i in range(length):
            index = numbers[i]%length if numbers[i] >= length else numbers[i]
            if numbers[index] > length:
                duplication[0] = index
                return True
            numbers[index] += length
        return False

a=Solution2()
a.duplicate([2,3,1,0,2,5,3],duplication=[0,0])