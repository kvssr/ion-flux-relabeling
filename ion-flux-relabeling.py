def solution(h, q):
		
	result = []
	
	length = (2**(h-1)*2-1)
			
	if h == 1:
		for x in q:
			result.append(-1)
		return result
	
	l = list(range(1, length +1))
	
	l2 = list(range(1, length +1))
	result2 = []
	for i in q:
		searchInt(l2, i, result)
	return result
  

def searchInt(l, i, result, parent = None):
	root = l[-1]
	if i > root:
		result.append(-1)
		return
	
	if root == i:
		if parent is not None:
			result.append(parent)
			return
		elif not parent:
			result.append(-1)
			return
	
	half = int((len(l)-1)/2)
	left = l[:half]
	right = l[half:-1]
	
	if half > 2:	
		if i <= left[-1]:
			searchInt(left, i, result, root)
			return
		else:
			searchInt(right, i, result, root)
			return
	else:
		if left[0] == i or right[0] == i:
			result.append(root)
			return
	return
