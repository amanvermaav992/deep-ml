
def orthogonal_projection(v, L):
	"""
	Compute the orthogonal projection of vector v onto line L.

	:param v: The vector to be projected
	:param L: The line vector defining the direction of projection
	:return: List representing the projection of v onto L
	"""
	import numpy as np
	addn = 0
	for i in L:
		addn += i**2
	addn = np.sqrt(addn)
	Lcap = [x/addn for x in L]
	dotprod = np.dot(v, Lcap)
	proj = [x*dotprod for x in Lcap]
	return proj
