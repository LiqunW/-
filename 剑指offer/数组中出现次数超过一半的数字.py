'''
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
思路：
1.哈希方法，记录每个数字出现的次数 时间空间复杂度O(n)
2.快拍的变种，每次找到长度大于原数组长度一半的数组，对该数组递归排序
3.一个candidate，用来保存数组中遍历到的某个数字；一个nTimes，表示当前数字的出现次数，其中，nTimes初始化为1。当我们遍历到数组中下一个数字的时候：
如果下一个数字与之前candidate保存的数字相同，则nTimes加1；
如果下一个数字与之前candidate保存的数字不同，则nTimes减1；
每当出现次数nTimes变为0后，用candidate保存下一个数字，并把nTimes重新设为1。 直到遍历完数组中的所有数字为止。
由于遍历一遍后得到的结果并不一定就是想要的，因此还要重新遍历，判断该数字是否出现超过一半

'''


class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if not numbers:
            return 0
        cnt=0
        for num in numbers:
            if cnt==0:
                tmp=num
                cnt=1
            elif tmp==num:
                cnt+=1
            elif tmp!=num:
                cnt-=1
        if cnt>=1:
            cnt=0
            for i in numbers:
                if i==tmp:
                    cnt+=1
        return tmp if cnt>len(numbers)//2 else 0