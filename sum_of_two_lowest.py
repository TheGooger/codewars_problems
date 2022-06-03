def sum_two_smallest_numbers(numbers):
	res_list = []
	for i in range(2):
		min_num = min(numbers)
		temp = numbers.pop(numbers.index(min_num))
		res_list.append(temp)
	return sum(res_list)
	
print(sum_two_smallest_numbers([2, 3, 4, 10]))
