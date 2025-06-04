import numpy as np
from scipy.linalg import lu
from utils.explainer import explain_step
from database.db import save_result

def lu_decomposition(A):
    P, L, U = lu(A)
    explanation = explain_step(A, L, U, 'lu')
    save_result("Lu", f"matriz={A}", f"P={P}, L={L}, U={U}", explanation)
    return (P, L, U), explanation