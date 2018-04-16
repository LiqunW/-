
def arrayPairSum(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums) // 2
    if n==1:
        return min(nums[0],nums[n])
    min1=nums[0]
    min2=nums[n]
    for i in range(n):
        j=i+n
        min1=min(nums[i],min1)
        min2=min(nums[j],min2)
    return min1+min2

output = arrayPairSum([1,4,3,2])
print(output)