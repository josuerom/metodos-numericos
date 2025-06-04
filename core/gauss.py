import numpy as np
from utils.explainer import explain_step
from database.db import save_result

def gauss_elimination(A, b):
    n = len(b)
    steps = []
    A = A.astype(float)
    b = b.astype(float)

    for i in range(n):
        if A[i][i] == 0.0:
            raise ValueError("Pivot cero encontrado.")
        for j in range(i+1, n):
            ratio = A[j][i]/A[i][i]
            A[j, :] -= ratio * A[i, :]
            b[j] -= ratio * b[i]
            steps.append(explain_step(A, b, i, j, ratio))

    x = np.zeros(n)
    x[-1] = b[-1]/A[-1][-1]

    for i in range(n-2, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i+1:], x[i+1:]))/A[i][i]

    save_result("Gauss", f"matriz={A}, términos={b}", f"x={x}, pasos={steps}", "Asistente IA")

    return x, steps