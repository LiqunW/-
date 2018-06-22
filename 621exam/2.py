import sys
import collections
def Solution(nums):
    haspresent={}
    count=0
    res=[]
    for i in nums:
        if count==10:
            break
        if i in haspresent:
            continue
        res.append(i)
        haspresent[i]=1
        count+=1
    res.insert(0, len(res))
    return res

if __name__ == "__main__":
    n=int(sys.stdin.readline().strip())
    nums=collections.deque()
    for i in range(n):
        line=sys.stdin.readline().strip()
        nums.append(int(line))
    out=Solution(nums)
    for i in out:
        print(i)