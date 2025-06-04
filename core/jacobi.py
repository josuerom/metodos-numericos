import numpy as np
from utils.explainer import explain_step
from database.db import save_result

def jacobi_method(A, b, x0=None, tol=1e-10, max_iter=100):
    n = len(b)
    x = np.zeros(n) if x0 is None else x0
    D = np.diag(A)
    R = A - np.diagflat(D)
    steps = []

    for i in range(max_iter):
        x_new = (b - np.dot(R, x)) / D
        steps.append(explain_step(x, x_new, i, 'jacobi'))
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            break
        x = x_new

    save_result("Jacobi", f"matriz={A}, términos={b}, x0={x0}, tol={tol}, max_iter={max_iter}", x, f"Asistente IA: cantidad de iteraciones realizadas {steps}.")
    return x, steps