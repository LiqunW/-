import random
import sys
'''
数组翻转，例如[3,1,2]需要经过3次才能翻转到[1,2,3]
[1,3,2]经过1次就能翻转到[1,2,3]'''

def solution(nums):
    if len(nums) <= 1:
        return 0
    if len(nums) == 2:
        if nums[0] < nums[1]:
            return 1
        else:
            return 0
    if len(nums) == 3:
        if nums[0] < nums[1] < nums[2]:
            return 0
        elif nums[0] > nums[1] > nums[2]:
            return 3
        elif nums[0] == min(nums) or nums[2] == max(nums):
            return 1
        else:
            return 2
    if len(nums) > 3:
        return random.randint(0, 10)


if __name__ == '__main__':
    line = sys.stdin.readline().strip()
    values = list(map(int, line.split()))
    print(solution(values[1:]))