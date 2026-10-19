def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	import numpy as np
	trace = matrix[0][0] + matrix[1][1]
	det = ((matrix[0][0])*(matrix[1][1])) - ((matrix[1][0])*(matrix[0][1]))
	l1 = (trace + (np.sqrt((trace**2)-(4*det))))/2
	l2 = (trace - (np.sqrt((trace**2)-(4*det))))/2
	eigenvalues = [float(l1), float(l2)]
	return eigenvalues