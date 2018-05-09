# 各种排序算法的Python实现

# 插入排序

'''  将一个数据插入排序数组中
	时间复杂度为O(n^2)
	是稳定的排序方式
'''

def insert_sort(array):
	count = len(array)
	for i in range(1,count):
		j = i-1
		key = array[i]
		while j >= 0:
			if array[j] > key:
				array[j],array[j+1] = key,array[j]
			j -= 1
	return array

output = insert_sort([1,3,-1,4,-2])
print(output)
# 希尔排序
''' 插入排序的改进版本，不稳定排序

'''

def shell_sort(array):
	count = len(array)
	gap = count //2
	while gap >= 1:
		for j in range(gap,count):
			i = j
			while (i - gap) >= 0:
				if array[i] < array[i-gap]:
					array[i],array[i-gap] = array[i-gap],array[i]
					i -= gap
				else:
					break
		gap //=2
	return array

# 冒泡排序
'''稳定排序'''

def bubble_sort(array):
	count = len(array)
	for i in range(count):
		for j in range(i+1,count):
			if array[i] > array[j]:
				array[i],array[j] = array[j], array[i]
	return array


# 快速排序
'''通过一趟排序把要排序的数据分成两部分，其中一部分的所有数据都比另一部分小，
然后再对这两部分进行快排，可以递归'''

def quick_sort(array):
	if not array:
		return []
	else:
		key=array[0]
		left=[x for x in array if x < key]
		right=[x for x in array[1:] if x >=key]
		return quick_sort(left)+[key]+quick_sort(right)



def quicksort2(array):
	left=[]
	right=[]
	middle=[]
	if len(array)<=1:
		return array
	else:
		mid=array[0]
		for i in array:
			if i < mid:
				left.append(i)
			elif i > mid:
				right.append(i)
			else:
				middle.append(i)
		left=quicksort2(left)
		right=quicksort2(right)
		return left + middle + right

#print(quicksort2([1,3,-1,2,5,0]))

# 直接选择排序
def select_sort(array):
	count = len(array)
	for i in range(count):
		min=i
		for j in range(i+1,count):
			if array[min]>array[j]:
				min=j
		array[min],array[i] = array[i],array[min]
	return array

# 堆排序 O(nlogn)  空间O(n)
'''
通常堆是通过一维数组来实现的。在阵列起始位置为0的情况中 
(1)父节点i的左子节点在位置(2*i+1); 
(2)父节点i的右子节点在位置(2*i+2); 
(3)子节点i的父节点在位置floor((i-1)/2);
堆可以分为大根堆和小根堆，这里用最大堆的情况来定义操作: 
(1)最大堆调整(MAX_Heapify):将堆的末端子节点作调整，使得子节点永远小于父节点。
这是核心步骤，在建堆和堆排序都会用到。比较i的根节点和与其所对应i的孩子节点的值。
当i根节点的值比左孩子节点的值要小的时候，就把i根节点和左孩子节点所对应的值交换，
当i根节点的值比右孩子的节点所对应的值要小的时候，就把i根节点和右孩子节点所对应的值交换。
然后再调用堆调整这个过程，可见这是一个递归的过程。 
(2)建立最大堆(Build_Max_Heap):将堆所有数据重新排序。建堆的过程其实就是不断做最大堆调整的过程，
从len/2出开始调整，一直比到第一个节点。 
(3)堆排序(HeapSort):移除位在第一个数据的根节点，并做最大堆调整的递归运算。
堆排序是利用建堆和堆调整来进行的。首先先建堆，然后将堆的根节点选出与最后一个节点进行交换，
然后将前面len-1个节点继续做堆调整的过程。直到将所有的节点取出，对于n个数我们只需要做n-1次操作。
'''
def heap_sort(lst):
	def sift_down(start, end):
		"""最大堆调整"""
		root = start
		while True:
			child = 2 * root + 1
			if child > end:
				break
			if child + 1 <= end and lst[child] < lst[child + 1]:
				child += 1
			if lst[root] < lst[child]:
				lst[root], lst[child] = lst[child], lst[root]
				root = child
			else:
				break
	# 创建最大堆
	for start in range((len(lst) // 2 - 1), -1, -1):
		sift_down(start, len(lst) - 1)
	# 堆排序
	for end in range((len(lst)-1),0,-1):
		lst[0],lst[end]=lst[end],lst[0]
		sift_down(0,end-1)
	return lst
def main():
	l = [8, 2, 1, 7, 6, 9, 5, 3,0 ,-3,4]
	print(heap_sort(l))
if __name__ == "__main__":
	main()

# 归并排序 分成分解和合并两个操作，合并两个有序数组简单
def merge_sort(array):
	if len(array)<=1:return array #最小分解到1
	num=int(len(array)/2)  #分成左右
	left = merge_sort(array[:num])
	right = merge_sort(array[num:])
	return merge(left,right)

def merge(left,right):
	# 合并两个已排序的数组
	l,r = 0,0
	result = []
	while l<len(left) and r<len(right):
		if left[l] < right[r]:
			result.append(left[l])
			l+=1
		else:
			result.append(right[r])
			r+=1
	result +=left[l:]
	result +=right[r:]
	return result

print(merge_sort([8, 2, 1, 7, 6, 9, 5, 3,0 ,-3,4]))