def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	means = []
	if mode == 'column':
		for i in range(len(matrix[0])):
			addn = 0
			for j in range(len(matrix)):
				addn += matrix[j][i]
			means.append(addn/(len(matrix)))
		
	elif mode == 'row':
		for i in range(len(matrix)):
			addn = 0
			for j in range(len(matrix[i])):
				addn += matrix[i][j]
			means.append(addn/(len(matrix[i])))
	return means