def myAtoi(str):
	"""
	:type str: str
	:rtype: int
	"""
	# 判断返回0的情况
	str = str.lstrip(' ')
	str = str.lstrip('0')
	if str == '' and  str[0] != '-' and str[0] != '+' and ('0'<=str[0]<='9')==False:
		return 0
	flag = 0;ans = []
	for i in str:
		if i == '+':
			flag = 1
			continue
		elif i == '-':
			flag = -1
			continue
		elif i < '0' or i > '9':
			break
		else:
			ans.append(i)
			ans.insert()
	res = int(''.join(ans))
	if flag == -1:
		return max(-res, -2 ** 31)
	else:
		return min(res, 2 ** 31 - 1)
print(myAtoi("words and 987"))
