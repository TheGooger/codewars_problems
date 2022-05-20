def solution(string, ending):
	"""Return True if first string argument ends with the 2nd one."""
	flag = False
	if len(ending) == 0:
		return True
	if len(string) >= len(ending):	
		for index in range(1, len(ending) + 1):
			if ending[-index] == string[-index]:
				flag = True
			else:
				return False
		return flag
	else:
		return False




#a = 'abcdef'
#for i in range(1, len(a) + 1):
#	print(a[-i])
