import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	XT = np.transpose(X)
	XT_X = np.matmul(XT, X)
	XT_Xinv = np.linalg.inv(XT_X)
	Xplus = np.matmul(XT_Xinv, XT)
	theta = Xplus @ y
	return theta