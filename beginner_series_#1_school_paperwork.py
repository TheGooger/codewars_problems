def paperwork(n, m):
	"""Counts how many blank pages I need. There are n classmates
	and m pages in paperwork."""
	if n > 0 and m > 0:
		return n * m
	return 0
