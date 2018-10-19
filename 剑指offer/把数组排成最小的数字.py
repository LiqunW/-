'''

'''
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers:
            return ''
        if len(numbers)==1:
            return numbers[0]
        for i in range(len(numbers)):
            for j in range(i+1,len(numbers)):
                if int(str(numbers[i])+str(numbers[j])) > int(str(numbers[j])+str(numbers[i])):
                    numbers[i],numbers[j]=numbers[j],numbers[i]
        return ''.join([str(i) for i in numbers])

a=Solution()
print(a.PrintMinNumber([3,32,321]))