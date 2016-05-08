def nth_last(a_list, n):
	if n <= len(a_list) and n > 0:
		print a_list[len(a_list) - n]
	else:
		print "null"
# nth_last([1,2,3], 2)
# nth_last([1,2,2], -1)
# nth_last([1,2,2], 7)
# nth_last([1,2,2], 0)


def secondToLast(a_list):
	nth_last(a_list, 2)

# secondToLast([1,2,3])
# secondToLast([7,8,"hello", 12])
# secondToLast([5])

def removeNeg(a_list):
	a_list = [val for val in a_list if val >= 0]
	print a_list

# removeNeg([1,-2,-3,12])

def nthLargest(a_list, n):
	