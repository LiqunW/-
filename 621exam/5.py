import sys
import collections

'''[10,20,30,60]从中找出n个数，使得和为100，返回值为[3,1,3,4]第一个3表示一共选了几个数，后面的数字是该数对应的index(1开始)'''
def solution(nums):
    if len(nums)==1:
        if nums[0]==100:
            return [1,1]
        else:
            return [0]

if __name__ == '__main__':
    n=int(sys.stdin.readline().strip())
    nums=collections.deque()
    for i in range(n):
        line=sys.stdin.readline().strip()
        nums.append(int(line))
    outputs=solution(nums)
    for i in outputs:
        print(i)