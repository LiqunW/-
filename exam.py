import sys

def find(N):
	X,Y = 0,0
	if N<=0:
		return (X,Y)
	for i in range(2,N+1,2):
		if N/i == int(N/i) and (N/i) % 2:
			X = int(N / i)
			Y = i
			break
	return (X,Y)

if __name__ == '__main__':
	#读取第一行的n
	n = int(sys.stdin.readline().strip())
	outputs = []
	inputs = []
	for i in range(n):
		val = int(sys.stdin.readline().strip())
		out = find(val)
		if out[0] or out[1]:
			print(out[0],out[1])
		else:
			print('No')