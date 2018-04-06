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
