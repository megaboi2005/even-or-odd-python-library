def iseven(num):
	try:
		int(num/2)
	except TypeError:
		return False
	return True:
def isodd(num):
	try:
		int(num/2)
		return False
	except TypeError:
		return True
