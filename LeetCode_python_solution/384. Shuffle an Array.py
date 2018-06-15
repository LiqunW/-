'''

Shuffle a set of numbers without duplicates.

Example:

// Init an array with set 1, 2, and 3.
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
solution.shuffle();

// Resets the array back to its original configuration [1,2,3].
solution.reset();

// Returns the random shuffling of array [1,2,3].
solution.shuffle();

题意：给出一个数组全排列中的一个数组，reset方法要求返回输入的数组，shuffle方法要求给出数组全排列的一种（等概率）
思路：reset方法返回输入数组即可，用swap，每次从[i,n-1]中随机一个数，和第i个数交换即可

'''
import copy
import random

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        shuffle_nums = copy.deepcopy(self.nums)
        for i in range(len(shuffle_nums)):
            j = random.randint(i,len(shuffle_nums)-1)
            shuffle_nums[i], shuffle_nums[j] = shuffle_nums[j], shuffle_nums[i]
        return shuffle_nums

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()